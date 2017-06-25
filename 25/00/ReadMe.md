# [10.9. データ圧縮](https://docs.python.jp/3/tutorial/stdlib.html#data-compression)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## ライブラリ

* [zlib](https://docs.python.jp/3/library/zlib.html#module-zlib)
* [gzip](https://docs.python.jp/3/library/gzip.html#module-gzip)
* [bz2](https://docs.python.jp/3/library/bz2.html#module-bz2)
* [lzma](https://docs.python.jp/3/library/lzma.html#module-lzma)
* [zipfile](https://docs.python.jp/3/library/zipfile.html#module-zipfile)
* [tarfile](https://docs.python.jp/3/library/tarfile.html#module-tarfile)

どれをどう使えばいいのかわからない。

### 参考

* http://qiita.com/wnoguchi/items/cb0fa7c11b119e96f1e5
* http://d.hatena.ne.jp/s-yata/20101023/1287938880
* http://qiita.com/supersaiakujin/items/c6b54e9add21d375161f

### アーカイブ形式

* tar

### 圧縮形式

* gz
* bz2
* lzma
* xz
* zip

### 圧縮の手順

1. 複数のファイルをtarで1ファイルにまとめる
1. tarファイルをgzip, bzip2, xzなどの各圧縮形式で圧縮する

#### tarで1ファイルにまとめる

* http://phantom37383.blog.fc2.com/blog-entry-1644.html

tarは以下のような特徴らしい。

* 圧縮機能はない
* 複数ファイルを1つにまとめる
    * パーミッション、更新日時、ユーザーグループ情報を保持できる
    
#### gzip, bzip2, xzはファイル単体にしか使えない

* gzip, bzip2, xzはファイル単体にしか使えない

複数ファイルがあるときは一度tarでまとめてから圧縮する必要がある。

## [zlib](https://docs.python.jp/3/library/zlib.html#module-zlib)

Python文書の例にあったコード。しかし圧縮形式にzlibなんてない。zlibとは何なのか。圧縮解凍できるようだが、ファイルではない？

```python
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))
```
```sh
$ python3 0.py 
41
37
b'witch which has which witches wrist watch'
226805979
```

41byteが37byteに圧縮できたということか？

[crc32()](https://docs.python.jp/3/library/zlib.html#zlib.crc32)はチェックサムを計算するらしい。チェックサムとは何か？

## [チェックサム](https://ja.wikipedia.org/wiki/%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF%E3%82%B5%E3%83%A0)

> チェックサム (Check Sum)とは誤り検出符号の一種である。符号値そのものを指すこともある。他の誤り検出符号と比べて信頼性は低いが、それでも単純計算で99.5%以上(1オクテットのチェックサムの場合255/256、2オクテットなら65535/65536)の検出率がある上にアルゴリズムが簡単であることから、簡易な誤り検出に用いられる。

> また、誤り検出その他データの検証のための符号として広く使われてきた経緯から、俗に誤り検出符号自体の代名詞としても用いられる場合がある。例えばCRCの符号値やMD5のハッシュ値を、それぞれ「CRCチェックサム」「MD5チェックサム」と呼ぶことがある。これらはアルゴリズムが異なりsumでもないため「チェックサム」と呼ぶことは、語義的には正確ではないものの、「（チェックサムよりも）信頼性の高い誤り検出符号」程度の意味で使われる。

### [誤り検出](https://ja.wikipedia.org/wiki/%E8%AA%A4%E3%82%8A%E6%A4%9C%E5%87%BA%E8%A8%82%E6%AD%A3)

> 誤り検出訂正（あやまりけんしゅつていせい）またはエラー検出訂正 (error detection and correction/error check and correct) とは、データに符号誤り（エラー）が発生した場合にそれを検出、あるいは検出し訂正（前方誤り訂正）することである。

難しくてよくわからない。予想してみる。圧縮すると同一データでなくなってしまう。でも同一かどうか確かめたい。そんなときにチェックサムを用いれば99.5%以上の確率で判定できる。ということか？

## [tarfile](https://docs.python.jp/3/library/tarfile.html#module-tarfile)

* http://mocobeta-backup.tumblr.com/post/83165051269/python-%E6%A8%99%E6%BA%96%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E6%8E%A2%E8%A8%AA-16-tarfile-%E7%B7%A8

```python
import pathlib
import tarfile

s = '圧縮対象データ。'
compression_format = 'gz' # gz, bz2, xz のいずれか xzだとエラーになった「tarfile.CompressionError: lzma module is not available」
file_name = '1.tar.{0}'.format(compression_format)
archive_path = pathlib.Path(file_name)

# 圧縮対象ファイルを適当につくる
def make_files():
    files = []
    for i in range(0,2):
        p = pathlib.Path(pathlib.PurePath('./in/file{0}.txt'.format(i))).resolve()
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
    tar.extractall(path=pathlib.Path('./out').resolve())
```
```sh
$ python 1.py 
```

以下のような構成。

* 1/
    * 1.py
    * in/
        * file0.txt
        * file1.txt
    * out/
        * in/
            * file0.txt
            * file1.txt
        * 1.tar.bz2
        * 1.tar.gz

file|byte
----|----
file0.txt|55
file1.txt|55
1.tar.bz2|229
1.tar.gz|201

* 圧縮ファイルのほうがサイズが大きくなった
    * おそらくフォルダやメタデータも保存しているからだろう
        * 圧縮対象ファイルのサイズが小さすぎると逆効果らしい
* gzのほうがbz2より圧縮されている。参考URLでは逆らしいのだが…

## [gzip](https://docs.python.jp/3/library/gzip.html#module-gzip), [bz2](https://docs.python.jp/3/library/bz2.html#module-bz2), [lzma](https://docs.python.jp/3/library/lzma.html#module-lzma)

```python
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
```
```sh
$ python3 2.py 
txt 41
gz  49
bz2 62
xz  92
```

ファイル|サイズ(byte)
--------|----------
2.txt|41
2.txt.gz|55
2.txt.bz2|62
2.txt.xz|92

圧縮するとサイズが大きくなってしまう。一体どのくらいのサイズから有用になるのか。

## [zipfile](https://docs.python.jp/3/library/zipfile.html#module-zipfile)モジュールを使わずにできてしまった。これらはファイル単体のときに使うのか？

```python
import zipfile

s = b'witch which has which witches wrist watch'
with zipfile.ZipFile('3.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('3.txt', s)
```
```sh
$ python3 3.py 
```

ファイル|サイズ(byte)
--------|----------
3.txt|41
3.zip|139

やはり圧縮ファイルのほうがサイズが大きい。

## まとめ

圧縮|compress()|file
----|----------|----
未圧縮|41|41
[zlib](https://docs.python.jp/3/library/zlib.html#module-zlib)|37|-
[gzip](https://docs.python.jp/3/library/gzip.html#module-gzip)|49|55
[bz2](https://docs.python.jp/3/library/bz2.html#module-bz2)|62|62
[lzma](https://docs.python.jp/3/library/lzma.html#module-lzma)|92|92
[zipfile](https://docs.python.jp/3/library/zipfile.html#module-zipfile)|-|139

Python文書の例にあった`zlib.compress()`だけが未圧縮より小さくなった。それ以外はむしろ肥大化してしまった。対象データが小さすぎるのが原因と思われる。

