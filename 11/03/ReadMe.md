# [7.2.1. ファイルオブジェクトのメソッド](https://docs.python.jp/3/tutorial/inputoutput.html#methods-of-file-objects)

< [7.2. ファイルを読み書きする](https://docs.python.jp/3/tutorial/inputoutput.html#reading-and-writing-files) < [7. 入力と出力](https://docs.python.jp/3/tutorial/inputoutput.html#input-and-output) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

> この節の以降の例は、 f というファイルオブジェクトが既に生成されているものと仮定します。

## メソッド

メソッド|説明
--------|----
`f.write()`|ファイルに書き込む。引数はopen()のmode次第でstrまたはbytes型。`f.write(str)`は書き込み文字数を返す。
`f.read()`|ファイルから読み取る
`f.readline()`|ファイルから1行だけ読み取る。ファイル終端=空文字, 空行=`\n`
`f.tell()`|ファイル先頭からの現在位置(byte数)。
`f.seek(offset, from_what)`|ファイル現在位置の変更。from_what=0:ファイル先頭(デフォルト), 1:現在位置, 2:ファイル終端。
`f.close()`|ファイルを閉じる。

## テキストファイルを1行ずつ読み込む

> ファイルから複数行を読み取るには、ファイルオブジェクトに対してループを書く方法があります。この方法はメモリを効率的に使え、高速で、簡潔なコードになります:

```python
with open('some.txt', 'w') as f:
    f.write("""one
two
three""")
with open('some.txt') as f:
    for i, line in enumerate(f):
        print(i, line, end='')
    print()
```
```
$ python 0.py 
0 one
1 two
2 three
```

`print()`は勝手に改行コードが付与される。テキストファイルは既に改行コードまで含まれている。そこで`end=''`により`print()`の改行を取り払うことで１行ずつ表示している。printとテキストファイル両方の改行があると以下のようになる。

```sh
$ python 0.py 
0 one

1 two

2 three
```

> ファイルのすべての行をリスト形式で読み取りたいなら、list(f) や f.readlines() を使うこともできます。

でもメモリ効率は悪いと。

## バイナリファイルのシーク

```python
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
```

```sh
$ python 1.py 
b'0123456789abcdef'
16 byte

0  b'0'
5  b'5'
6  b'6'
0  b'0'
16  b''
15  b'f'
```

## with

> with を使うと、処理中に例外が発生しても必ず最後にファイルを閉じることができます。同じことを try-finally を使って書くよりずっと簡潔に書けます:

withを使えるときは使ったほうが良い。
