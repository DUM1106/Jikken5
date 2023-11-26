import os

def rename_files(folder_path):
    # 指定したフォルダ内のファイル一覧を取得
    files = os.listdir(folder_path)

    # ファイルごとに処理
    for file_name in files:
        # ファイルのフルパスを構築
        old_path = os.path.join(folder_path, file_name)

        # VOICEACTRESS100_003 の部分を取り出す
        new_name = file_name.split('-')[0]+".mp3"

        # 新しいファイル名のフルパスを構築
        new_path = os.path.join(folder_path, new_name)

        # ファイル名の変更
        os.rename(old_path, new_path)
        print(f'Renamed: {file_name} -> {new_name}')

# フォルダのパスを指定してファイル名を変更
folder_path = 'voicechanged/jvs097'
rename_files(folder_path)