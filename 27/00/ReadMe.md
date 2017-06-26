# [11.1. 出力のフォーマット](https://docs.python.jp/3/tutorial/stdlib2.html#output-formatting)

< [11. 標準ライブラリミニツアー — その 2](https://docs.python.jp/3/tutorial/stdlib2.html#brief-tour-of-the-standard-library-part-ii) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

> ツアーの第2部では、プロフェッショナルプログラミングを支えるもっと高度なモジュールをカバーします。ここで挙げるモジュールは、小さなスクリプトの開発ではほとんど使いません。

## [reprlib](https://docs.python.jp/3/library/reprlib.html#module-reprlib)

[reprlib](https://docs.python.jp/3/library/reprlib.html#module-reprlib)は[repr()](https://docs.python.jp/3/library/functions.html#repr)に似た関数を実装するために役に立つらしい。[repr()](https://docs.python.jp/3/library/functions.html#repr)はオブジェクトの印字可能な表現を含む文字列を返す。

```python
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
```
```sh
$ python 0.py 
```
何も表示されない。

### @reprlib.recursive_repr()

```python
import reprlib
class MyList(list):
    @reprlib.recursive_repr()
    def __repr__(self):
        return '<' + '|'.join(map(repr, self)) + '>'

m = MyList('abc')
m.append(m)
m.append('x')
print(m)
```

リンク先で最初に見つかったコードにimport文を足した。これまでチュートリアルではアノテーションについての説明が無かったと思う。`@reprlib.recursive_repr()`についてさっぱりわからない。構文説明せず、動作する完全なコードも書かない。結果的に動作確認さえできず苦労させられる。

## [pprint](https://docs.python.jp/3/library/pprint.html#module-pprint)

> 表示結果が複数行にわたる場合は、 “pretty printer” と呼ばれるものが改行やインデントを追加して、データ構造がより明確になるように印字します

```python
import pprint
import sys
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t)
print('')
pprint.pprint(t, compact=False)
print('')
pprint.pprint(t, width=-1, compact=True)
print('')
pprint.pprint(t, width=10000, compact=True)
print('')
pprint.pprint(t, width=30)
print('')
pprint.pprint(t, indent=4)
print('')
pp = pprint.PrettyPrinter(indent=4, width=sys.maxsize, depth=sys.maxsize, compact=True)
pp.pprint(t)
print('')
```
```sh
$ python 2.py 
[[[['black', 'cyan'], 'white', ['green', 'red']],
  [['magenta', 'yellow'], 'blue']]]

[[[['black', 'cyan'], 'white', ['green', 'red']],
  [['magenta', 'yellow'], 'blue']]]

[[[['black',
    'cyan'],
   'white',
   ['green',
    'red']],
  [['magenta',
    'yellow'],
   'blue']]]

[[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]

[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]

[   [   [['black', 'cyan'], 'white', ['green', 'red']],
        [['magenta', 'yellow'], 'blue']]]

[[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
```

http://enajet.air-nifty.com/blog/2011/09/python-9a0e-1.html

### json

jsonの場合はpprintでなく`json.dumps(dict, indent=4)`を使ったほうが良い。

```python
import json
import pprint
import sys
j = [{'name': 'Yamada', 'age': '100'}, {'name': 'Suzuki', 'age': '99'}, {'name': 'Tanaka', 'age': '88'}]
js = json.dumps(j)
print(js)
print('')
print(json.dumps(j, indent=4))
print('')

pprint.pprint(js)
print('')
pprint.pprint(js, compact=True)
print('')
pprint.pprint(js, width=-1, compact=True)
print('')
pprint.pprint(js, width=10000, compact=True)
print('')
pprint.pprint(js, width=30)
print('')
pprint.pprint(js, indent=4)
print('')
pp = pprint.PrettyPrinter(indent=4, width=sys.maxsize, depth=sys.maxsize, compact=True)
pp.pprint(js)
print('')
```
```sh
$ python 3.py 
[{"name": "Yamada", "age": "100"}, {"name": "Suzuki", "age": "99"}, {"name": "Tanaka", "age": "88"}]

[
    {
        "name": "Yamada",
        "age": "100"
    },
    {
        "name": "Suzuki",
        "age": "99"
    },
    {
        "name": "Tanaka",
        "age": "88"
    }
]

('[{"name": "Yamada", "age": "100"}, {"name": "Suzuki", "age": "99"}, {"name": '
 '"Tanaka", "age": "88"}]')

('[{"name": "Yamada", "age": "100"}, {"name": "Suzuki", "age": "99"}, {"name": '
 '"Tanaka", "age": "88"}]')

('[{"name": '
 '"Yamada", '
 '"age": '
 '"100"}, '
 '{"name": '
 '"Suzuki", '
 '"age": '
 '"99"}, '
 '{"name": '
 '"Tanaka", '
 '"age": '
 '"88"}]')

'[{"name": "Yamada", "age": "100"}, {"name": "Suzuki", "age": "99"}, {"name": "Tanaka", "age": "88"}]'

('[{"name": "Yamada", "age": '
 '"100"}, {"name": "Suzuki", '
 '"age": "99"}, {"name": '
 '"Tanaka", "age": "88"}]')

('[{"name": "Yamada", "age": "100"}, {"name": "Suzuki", "age": "99"}, {"name": '
 '"Tanaka", "age": "88"}]')

'[{"name": "Yamada", "age": "100"}, {"name": "Suzuki", "age": "99"}, {"name": "Tanaka", "age": "88"}]'
```

## [textwrap](https://docs.python.jp/3/library/textwrap.html#module-textwrap)

> 段落で構成された文章を、指定したスクリーン幅にぴったり収まるように調整します

### 英文

```python
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
```
```sh
$ python 4.py 
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

ぴったりではなく、指定字数を超えないように半角スペース単位で区切るらしい。

### 和文

```python
import textwrap
doc = """textwrapは指定字数に改行コードを挿入した文字列を返すらしい。ただし丁度その字数目ではない。単語単位で区切る。単語は半角スペース区切りで識別される英語仕様。日本語ではどうなるか。"""
print(textwrap.fill(doc, width=40))
```
```sh
$ python 5.py 
textwrapは指定字数に改行コードを挿入した文字列を返すらしい。ただし丁度そ
の字数目ではない。単語単位で区切る。単語は半角スペース区切りで識別される英語仕様
。日本語ではどうなるか。
```

* 日本語の文章は単語を半角スペースで区切って書かない
    * 単語ごとに分割してくれない
    * 40文字目の後ろに改行コードが挿入されるだけ
* 1byte文字と2byte文字の幅を考慮しない
    * それが考慮され、かつ等幅フォントであるなら印字幅を統一できたのに…

英語仕様のAPIであり日本語では使いづらい。日本語の文章は半角文字と併用になる。この仕様だと役に立たない。微妙な使用感。

## [locale](https://docs.python.jp/3/library/locale.html#module-locale)

```python
import locale
#locale.setlocale(locale.LC_ALL, 'English_United States.1252') # locale.Error: unsupported locale setting
print(locale.setlocale(locale.LC_ALL, ''))
conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping=True)) # '1,234,567'
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))
print(locale.currency(1000000, grouping=True))
```
```sh
$ python 6.py 
ja_JP.UTF-8
1,234,567
￥1,234,568
￥1,000,000
```

* http://qiita.com/atsaki/items/2a6ad84b319010758666

### [円記号問題](https://ja.wikipedia.org/wiki/%E5%86%86%E8%A8%98%E5%8F%B7#Unicode.E3.81.8C.E6.8C.81.E3.81.A4.E5.95.8F.E9.A1.8C.EF.BC.88.E5.86.86.E8.A8.98.E5.8F.B7.E5.95.8F.E9.A1.8C.EF.BC.89)

円記号が全角で表示されるのがダサい。数字は半角なので統一感がない。[円記号問題](https://ja.wikipedia.org/wiki/%E5%86%86%E8%A8%98%E5%8F%B7#Unicode.E3.81.8C.E6.8C.81.E3.81.A4.E5.95.8F.E9.A1.8C.EF.BC.88.E5.86.86.E8.A8.98.E5.8F.B7.E5.95.8F.E9.A1.8C.EF.BC.89)のとおり、私のLinux環境では半角円記号はバックスラッシュで表示される。

Wikipediaの[符号位置](https://ja.wikipedia.org/wiki/%E5%86%86%E8%A8%98%E5%8F%B7#.E7.AC.A6.E5.8F.B7.E4.BD.8D.E7.BD.AE)からコピペすると半角円記号を表示できた。

記号|Unicode
----|-------
`¥`|U+00A5
`￥`|U+FFE5
`\`|U+005C

IMEで入力できないのが原因か。キーボードには右Shiftキーの左にバックスラッシュ用キーがあるのに、円記号キーまでバックスラッシュが入力されてしまう。

