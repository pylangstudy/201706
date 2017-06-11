file_path = '1.bin'
with open(file_path, 'wb') as f:
    data = b'0123456789abcdef'
    print(data)
    print(f.write(data), end=' byte\n\n')
with open(file_path, 'rb') as f:
    print(f.tell(), end='  ')
    print(f.read(1))

    print(f.seek(5), end='  ')
    print(f.read(1))

    print(f.seek(0, 1), end='  ') # 1: 現在位置
    print(f.read(1))

    print(f.seek(0, 0), end='  ') # 0: ファイル先頭
    print(f.read(1))

    print(f.seek(0, 2), end='  ') # 2: ファイル末尾
    print(f.read(1))

    print(f.seek(-1, 2), end='  ') # 2: ファイル末尾
    print(f.read(1))

