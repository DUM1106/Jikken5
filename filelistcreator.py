file_list_path = "filelists/ljs_audio_val_filelist.txt"
speaker_id = "jvs100"
voice_description = "この男性は普通の高さで、普通の速さで話します。大人の雰囲気があり、かっこいい雰囲気を持ちつつ、流暢で爽やかで明瞭な発音があります。"

with open(file_list_path, 'a') as file:
    for i in range(1, 101):
        file.write(f"jvs_ver1/{speaker_id}/parallel100/wav24kHz16bit/VOICEACTRESS100_{i:03d}.wav|{voice_description}\n")

print(f"ファイルが {file_list_path} に正常に追加されました。")