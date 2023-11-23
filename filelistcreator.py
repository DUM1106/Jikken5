file_list_path = "filelists/ljs_audio_test_filelist.txt"
speaker_id = "jvs001"
voice_description = "この男性は普通の高さで、遅い速さで話します。大人の雰囲気があり、太い声でかっこいい印象を与えます。流暢で明瞭な発音があります。"

with open(file_list_path, 'a') as file:
    for i in range(1, 101):
        file.write(f"jvs_ver1/{speaker_id}/parallel100/wav24kHz16bit/VOICEACTRESS100_{i:03d}.wav|{voice_description}\n")

print(f"ファイルが {file_list_path} に正常に追加されました。")