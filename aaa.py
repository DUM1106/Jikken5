import random
import re


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    pattern = re.compile(r'(jvs[^|]+\.wav)\|jvs[^|]+\.wav\|')
    processed_lines = [pattern.sub(r'\1|', line) for line in lines]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)


process_file('./filelists/ljs_audio_test_filelist.txt')
