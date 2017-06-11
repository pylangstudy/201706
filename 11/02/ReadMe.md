# [7.2. ファイルを読み書きする](https://docs.python.jp/3/tutorial/inputoutput.html#reading-and-writing-files)

< [7. 入力と出力](https://docs.python.jp/3/tutorial/inputoutput.html#input-and-output) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## `open()`

> [open()](https://docs.python.jp/3/library/functions.html#open) は [file object](https://docs.python.jp/3/glossary.html#term-file-object) を返します。

### 書き込み

```python
with open('some.txt', 'w') as f:
    f.write('Write!!')
```

### 読み込み

```python
with open('some.txt') as f:
    print(f.read())
```

### モードと文字コードの指定

```python
with open('some.txt', mode='r', encoding='utf-8') as f:
    print(f.read())
```

mode|説明
----|----
`r`|読込専用。書込できない。
`w`|書込専用。ファイル全体を丸ごと上書きする。
`a`|追記モード。ファイル末尾に追記する。
`r+`|読み書き両用。

### バイナリファイル

modeの後ろに`b`をつける。binaryの略と思われる。省略した時は`t`(`text`の略と思われる)として解釈される。

```python
with open('some.bin', 'wb') as f:
    f.write(bytearray([0xFF, 0x12, 0x89]))
```
```python
with open('some.txt', 'rb') as f:
    print(f.read())
```

テキスト以外はバイナリモードで扱うべき。

#### バイナリファイルの書き込み

http://qiita.com/norioc/items/6c6fbecc2ece6d1dc8e3

```python
import struct
with open('some.bin', 'wb') as f:
    for x in [0xFF, 0x12, 0x89]:
        f.write(struct.pack("B", x))
    f.write(bytearray([0xFF, 0x12, 0x89]))
with open('some.bin', 'rb') as f:
    print(f.read())
```
```sh
$ hexdump some.bin
0000000 12ff ff89 8912                         
0000006
```

