import os
from pydub import AudioSegment

def convert_mp3_to_wav(directory):
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is an MP3
            if file.lower().endswith('.mp3'):
                mp3_path = os.path.join(root, file)
                # Remove the .mp3 extension and add 'changed' to the start
                base_name = os.path.splitext(file)[0]
                wav_file_name = f"{base_name}.wav"
                wav_path = os.path.join(root, wav_file_name)

                # Load MP3 file
                mp3_audio = AudioSegment.from_file(mp3_path, format="mp3")

                # Set frame rate
                wav_audio = mp3_audio.set_frame_rate(24000)

                # Export as WAV
                wav_audio.export(wav_path, format="wav")
                print(f"Converted '{mp3_path}' to '{wav_path}'")

#Replace 'your_directory_path' with the path to the directory containing the MP3 files
convert_mp3_to_wav('voicechanged_val/jvs016')
#jvs002 59
#jvs004 70
#jvs005 15 16 26 