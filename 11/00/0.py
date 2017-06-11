import sys

print('abc')
print(sys.stdout)
#print(sys.stdout.read()) # io.UnsupportedOperation: not readable
#with open(sys.stdout, mode='r', encoding='utf-8') as f:  # TypeError: expected str, bytes or os.PathLike object, not _io.TextIOWrapper
#    print(f.read())

file_path = 'stdout.txt'
sys.stdout = open(file_path, 'w')
print('defghijk')
sys.stdout.close()
sys.stdout = sys.__stdout__
with open(file_path) as f:
    print(f.read())

