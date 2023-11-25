import os
import random

def modify_file_content(input_file_path, output_file_path):
    # ファイルを読み込む
    with open(input_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # wavファイル名を抽出し、jvs番号とともに保存
    wav_files = {}
    for line in lines:
        parts = line.strip().split('|')
        wav_file = parts[0].strip()
        jvs_number, rest = wav_file.split('/')[1], '/'.join(wav_file.split('/')[2:])
        if rest not in wav_files:
            wav_files[rest] = []
        wav_files[rest].append(jvs_number)

    # 各行を変更する
    modified_lines = []
    for line in lines:
        parts = line.strip().split('|')
        wav_file = parts[0].strip()
        rest = '/'.join(wav_file.split('/')[2:])
        if len(wav_files[rest]) > 1:
            # 同じwavファイルに対する異なるjvs番号をランダムに選ぶ
            other_jvs_numbers = [jvs for jvs in wav_files[rest] if jvs not in wav_file]
            other_jvs = random.choice(other_jvs_numbers)
            new_wav_file = wav_file.replace(wav_file.split('/')[1], other_jvs, 1)
            modified_line = f"{wav_file}|{new_wav_file}|{'|'.join(parts[1:])}"
        else:
            modified_line = line.strip()
        modified_lines.append(modified_line)

    # 変更された内容を新しいファイルに書き込む
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for line in modified_lines:
            f.write(line + '\n')

# この関数を使用してファイルの内容を変更します
modify_file_content('./filelists/ljs_audio_val_filelist.txt', './filelists/ljs_audio_val_filelist.txt')
