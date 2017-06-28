# [11.3. バイナリデータレコードの操作](https://docs.python.jp/3/tutorial/stdlib2.html#working-with-binary-data-record-layouts)

< [11. 標準ライブラリミニツアー — その 2](https://docs.python.jp/3/tutorial/stdlib2.html#brief-tour-of-the-standard-library-part-ii) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [struct](https://docs.python.jp/3/library/struct.html#module-struct)

* [pack()](https://docs.python.jp/3/library/struct.html#struct.pack)
* [unpack()](https://docs.python.jp/3/library/struct.html#struct.unpack)

### zipファイル解析

以下の例では、 [zipfile](https://docs.python.jp/3/library/zipfile.html#module-zipfile) モジュールを使わずに、ZIP ファイルのヘッダ情報を 巡回する方法を示しています。

> "H" と "I" というパック符号は、それぞれ2バイトと4バイトの符号無し 整数を表しています。 "<" は、そのパック符号が standard サイズであり、バイトオーダーが リトルエンディアンであることを示しています:

適当にZIPファイルを用意する。以下ファイルをファイラでZIPに圧縮して`0.txt.zip`ファイルを作成した。

0.txt
```
0.txtをZIP圧縮する。
```

```python
import struct

with open('0.txt.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```
```sh
$ python3 0.py 
b'0.txt' 0xc18c44cc 27 27
b'' 0x44cc4adc 1819020 1769472
Traceback (most recent call last):
  File "0.py", line 9, in <module>
    fields = struct.unpack('<IIIHH', data[start:start+16])
struct.error: unpack requires a bytes object of length 16
```

エラーが出たが、途中までは解析できているっぽい。「b'0.txt' 0xc18c44cc 27 27」という部分で`0.txt`とファイル名が表示された。

以下がポイントのようだ。`<IIIHH`でバイト配列を表しているらしい。
```python
fields = struct.unpack('<IIIHH', data[start:start+16])
```

この例題を読み解くには以下の知識が必要。

* コンピュータのデータ形式
    * 2進数
        * バイナリの概念
            * バイトオーダーの概念
                * アラインメントの概念
* ZIPファイルのバイナリ形式仕様

[struct](https://docs.python.jp/3/library/struct.html#module-struct)ではバイト配列を`<IIIHH`のように独自の文字を使って表現するようだ。

別途Markdownファイルに[コンピュータのデータ形式](https://github.com/pylangstudy/201706/blob/master/28/01/Computer.md)についてメモした。

