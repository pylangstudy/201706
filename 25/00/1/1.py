import pathlib
import tarfile

s = '圧縮対象データ。'
compression_format = 'gz' # gz, bz2, xz のいずれか xzだとエラーになった「tarfile.CompressionError: lzma module is not available」
file_name = '1.tar.{0}'.format(compression_format)
archive_path = pathlib.Path(file_name)
pathlib.Path(pathlib.PurePath('./in/')).mkdir(parents=True, exist_ok=True)
pathlib.Path(pathlib.PurePath('./out/')).mkdir(parents=True, exist_ok=True)

# 圧縮対象ファイルを適当につくる
def make_files():
    files = []
    for i in range(0,2):
        p = pathlib.Path(pathlib.PurePath('./in/file{0}.txt'.format(i)))
        if not p.is_file():
            with open(p, mode='w', encoding='utf-8') as f:
                f.write('ファイルの内容。圧縮対象データ。{0}'.format(i))
        files.append(p)
    return files

# ファイルを圧縮する
with tarfile.open('./out' / archive_path, 'w:{0}'.format(compression_format)) as tar:
    for path in make_files():
        if path.is_file(): tar.add(path)

# 圧縮ファイルを解凍する
with tarfile.open('./out' / archive_path, 'r') as tar:
    
    import os
    
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tar, path=pathlib.Path("./out").resolve())

