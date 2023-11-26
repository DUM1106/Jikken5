import random
import re


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    pattern = re.compile(r'(jvs[^|]+\.wav)\|jvs[^|]+\.wav\|')
    processed_lines = [pattern.sub(r'\1|', line) for line in lines]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)


process_file('sljs_audio_val_filelist.txt')

def process_text_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            parts = line.strip().split('|')
            if len(parts) == 2:
                # ファイルパスの変更
                new_path = f"voicechanged/{parts[0].split('/')[1]}/{parts[0].split('/')[4]}"
                # 新しい行の書き込み
                outfile.write(f"{parts[0]}|{new_path}|{parts[1]}\n")
            else:
                # 2つのパイプで区切られていない行はそのまま書き込み
                outfile.write(line)

input_file_path = "sljs_audio_val_filelist.txt"
output_file_path = "ljs_audio_val_filelist.txt"
process_text_file(input_file_path, output_file_path)