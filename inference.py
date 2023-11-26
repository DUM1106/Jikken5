from utils import load_wav_to_torch
from mel_processing import spectrogram_torch
import IPython.display as ipd
import numpy as np
import soundfile as sf
import torch
import utils
from models import SynthesizerTrn
from text.symbols import symbols

hps = utils.get_hparams()

net_g = SynthesizerTrn(
    len(symbols),
    hps.data.filter_length // 2 + 1,
    hps.train.segment_size // hps.data.hop_length,
    **hps.model).cuda()
_ = net_g.eval()

_ = utils.load_checkpoint("./logs/ljs_base/G_4800.pth", net_g, None)

#プロンプトを入れる
x = '男性、声が高い、可愛い'
#音声データのパスを入れる
file_path = 'voicechanged/jvs001/VOICEACTRESS100_001.wav'

#スペクトログラムファイルを計算して保存
audio, sampling_rate = load_wav_to_torch(file_path)
audio_norm = audio / hps.data.max_wav_value
audio_norm = audio_norm.unsqueeze(0)
audio_norm = audio_norm.cuda()

spec_filename = file_path.replace(".wav", ".spec.pt")
spec = spectrogram_torch(audio_norm, hps.data.filter_length, hps.data.sampling_rate, hps.data.hop_length, hps.data.win_length, center = False)
spec = spec.unsqueeze(0)
spec = torch.view_as_real(spec).abs()  # Convert to magnitude if complex
spec = torch.sqrt(spec[..., 0]**2 + spec[..., 1]**2)
spec=spec.cuda()
torch.save(spec, spec_filename)

#spec_lengths計算
batch = 1
max_spec_len =spec.size(1)
spec_lengths = torch.LongTensor([max_spec_len])
spec_lengths = spec_lengths.cuda()
y = spec.cuda()
y_lengths = spec_lengths.cuda()
with torch.no_grad():
    # Perform the inference
    output = net_g.infer(x, y, y_lengths)

    # Unpack the output
    o, y_mask, (z, m_q, logs_q) = output

    # Assuming 'o' contains the audio data you want, and it's the first tensor in the tuple
    audio = o[0].data.cpu().float().numpy()


from scipy.io import wavfile
sampling_rate = int(hps.data.sampling_rate)

# Squeeze the audio array to remove the single-channel dimension
audio = audio.squeeze()

# Ensure the audio array is now 1D
print(audio.shape)  # Should be (200763,)

# Write the audio to a WAV file
wav_output_filename = 'output_audio.wav'
wavfile.write(wav_output_filename, sampling_rate, audio)
print(f"Audio file saved as {wav_output_filename}")


ipd.display(ipd.Audio(audio, rate=hps.data.sampling_rate, normalize=False))