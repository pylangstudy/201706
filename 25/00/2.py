import gzip
import bz2
import lzma

s = b'witch which has which witches wrist watch'
with open('2.txt', 'wb') as f: f.write(s)
with gzip.open('2.txt.gz', 'wb') as f: f.write(s)
with bz2.open('2.txt.bz2', 'wb') as f: f.write(s)
with lzma.open('2.txt.xz', 'wb') as f: f.write(s)

print('txt', len(s))
print('gz ', len(gzip.compress(s)))
print('bz2', len(bz2.compress(s)))
print('xz ', len(lzma.compress(s)))

