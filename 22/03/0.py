import os
print(os.getcwd()) # Get Current Working Directory
print(os.system('mkdir some')) # シェルコマンド 戻り値: 0(正常終了), 256(mkdir: ディレクトリ `some' を作成できません: ファイルが存在します)
print(os.chdir('/tmp/some'))  # Change Current Working Directory 戻り値: None
print(os.getcwd())

