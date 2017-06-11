# [7.1. 出力を見やすくフォーマットする](https://docs.python.jp/3/tutorial/inputoutput.html#fancier-output-formatting)

[7. 入力と出力](https://docs.python.jp/3/tutorial/inputoutput.html#input-and-output) < [6. モジュール (module)](https://docs.python.jp/3/tutorial/modules.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 既出の出力メソッド

* [print()](https://docs.python.jp/3/library/functions.html#print)
* `open('path').write()`

## 標準出力の参照

* `sys.stdout`

> 詳細はライブラリリファレンスを参照してください。

とあるが、探してみると[説明がなかった](https://docs.python.jp/3/library/sys.html#sys.stdout)。何を参照しろと……。仕方ないのでググる。

http://d.hatena.ne.jp/alicehimmel/20110213/1297611415

`sys.stdout`はファイルオブジェクトらしい。出力した内容を参照できる。が、別のファイルオブジェクトにしないと参照できないらしい。

```python
file_path = 'stdout.txt'
sys.stdout = open(file_path, 'w')
print('defghijk')
sys.stdout.close()
sys.stdout = sys.__stdout__
with open(file_path) as f:
    print(f.read())
```

気軽には使えない。

## フォーマット方法

* [print()](#print())
* [str.format()](https://docs.python.jp/3/library/stdtypes.html#str.format)
* [フォーマット済み文字列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#f-strings)
* [string](https://docs.python.jp/3/library/string.html#module-string)モジュールの[Template](https://docs.python.jp/3/library/string.html#string.Template)クラス

### print()

```python
>>> print('abc', 'def', 'ghi')
abc def ghi
```
print文は可変長引数を受け取れる。出力したい内容を渡してやると、スペース区切りでフォーマットしてくれる。

### str.format()

```python
>>> "a{0}b".format('ABC')
'aABCb'
```

#### 順固定

```python
>>> 'a{}b{}'.format('ABC', 'DEF')
'aABCbDEF'
```

#### 順不問

```python
>>> "a{1}b{2}".format('ABC', 'DEF')
'aABCbDEF'
```
```python
>>> "a{1}b{0}".format('ABC', 'DEF')
'aDEFbABC'
```

#### 名前付き

```python
>>> "a{v1}b".format(v1='ABC')
'aABCb'
```
```python
>>> "a{v1}b{v2}".format(v1='ABC', v2='DEF')
'aABCbDEF'
```
```python
>>> "a{v2}b{v1}".format(v1='ABC', v2='DEF')
'aDEFbABC'
```

#### 併用

```python
>>> "a{0}b{value}".format('ABC', value='DEF')
'aABCbDEF'
```

##### `{}`と`{番号}`は併用できない

```python
>>> "a{}b{0}".format('ABC', 'DEF')
ValueError: cannot switch from automatic field numbering to manual field specification
>>> "a{}b{0}".format('ABC')
ValueError: cannot switch from automatic field numbering to manual field specification
>>> "a{}b{1}".format('ABC')
ValueError: cannot switch from automatic field numbering to manual field specification
>>> "a{}b{1}".format('ABC', 'DEF')
ValueError: cannot switch from automatic field numbering to manual field specification
```

### フォーマット済み文字列リテラル

3.6で追加されたらしい。

```python
>>> value = 'ABC'
>>> f"{value}"
'ABC'
>>> print(f"{value}")
ABC
```

記法|コード
----|------|
str.format()|`"{value}".format(value=value)`
フォーマット済み文字列リテラル|`f"{value}"`

任意の変数名をそのままフォーマットでも使える。名前付きでありながら冗長さを解決している。

### [string](https://docs.python.jp/3/library/string.html#module-string)モジュールの[Template](https://docs.python.jp/3/library/string.html#string.Template)クラス

```python
from string import Template

markdown_template = """# $Overview 

$Details"""
t = Template(markdown_template)
print( t.substitute(Overview='これは概要タイトルである', Details='これは詳細な説明文である。') )
```
```sh
$ python 1.py 
# これは概要タイトルである 

これは詳細な説明文である。
```

こんな便利クラスがあったとは知らなかった。テンプレートエンジン不要か。

## 細かいこと

### 数値→文字列

> Python には値を文字列に変換する方法があります。値を [repr()](https://docs.python.jp/3/library/functions.html#repr) か [str()](https://docs.python.jp/3/library/functions.html#repr) 関数に渡してください。

```python
>>> str(123)
'123'
>>> repr(123)
'123'
```

### str()とrepr()の違い

> 多くの値がどちらの関数に対しても同じ表現を返します。一方、文字列は、2つの異なる表現を持っています。

```python
>>> str('abc')
'abc'
>>> repr('abc')
"'abc'"
```
```python
>>> str('ab\ncd')
'ab\ncd'
>>> repr('ab\ncd')
"'ab\\ncd'"
```

repr()は`\`によるエスケープ文字もそのまま出力するらしい。

### 右寄せ

#### [str.rjust()](https://docs.python.jp/3/library/stdtypes.html#str.rjust)

[str.rjust()](https://docs.python.jp/3/library/stdtypes.html#str.rjust)は右寄せする。

```python
>>> str(1).rjust(3)
'  1'
>>> str(12).rjust(3)
' 12'
>>> str(123).rjust(3)
'123'
```

#### str.format()

```python
>>> '{0:3d}'.format(1)
'  1'
>>> '{0:3d}'.format(12)
' 12'
>>> '{0:3d}'.format(123)
'123'
```

### ゼロ埋め

```python
>>> '1'.zfill(3)
'001'
>>> '12'.zfill(3)
'012'
>>> '123'.zfill(3)
'123'
```

### str.format()のフォーマット書式

#### フォーマット前に変換する

##### `{!a}`

[ascii()](https://docs.python.jp/3/library/functions.html#ascii)する。

```python
>>> '{!a}'.format('ABC')
"'ABC'"
>>> '{!a}'.format('山田')
"'\\u5c71\\u7530'"
```

##### `{!s}`

[str()](https://docs.python.jp/3/library/stdtypes.html#str)する。

```python
>>> '{!s}'.format(123)
'123'
>>> '{!s}'.format(ABC)
NameError: name 'ABC' is not defined
```

数値を文字列化するときに使う。

##### `{!r}`

[repr](https://docs.python.jp/3/library/functions.html#repr)する。

```python
>>> '{!r}'.format('AB\nCD')
"'AB\\nCD'"
```

エスケープ文字もそのまま出す。

#### 桁数指定

##### 数値

円周率πを、小数点以下2桁で丸めてフォーマット。

```python
>>> import math
>>> math.pi
3.141592653589793
>>> '{0:.2f}'.format(math.pi)
'3.14'
```

##### 文字列

> フィールドの最低の文字幅を指定できます。

```python
#d = {'山田太郎': 123, '三下五郎丸のすけ': 456789}
d = {'ABC': 123, 'DEFGHIJ': 456789}
for n, v in d.items():
    print('{0:8}|{1:8d}'.format(n, v))
```
```python
$ python 2.py 
ABC     |     123
DEFGHIJ |  456789
```
```python
$ python 2.py 
山田      |     123
三下五郎    |  456789
```

> 綺麗なテーブルを作るのに便利です。

ただし以下の条件が必須。

* 1byte幅文字であること（日本語などの2byte幅文字を使うとズレる）
* 等幅フォントであること

半角スペース埋めされるが、半角スペースは1byte幅である。2byte幅文字とのズレが生じてしまう。日本語では使えない。

#### 辞書参照

##### キー参照

```python
d = {'name': 'Yamada', 'age': 123}
print('{0[name]:8s}|{0[age]:4d}'.format(d))
```
```sh
$ python 3.py 
Yamada  | 123
```

複数の辞書に対してループしてみる。
```python
d = [{'name': 'Yamada', 'age': 123}, {'name': 'Takahashi', 'age': 88}]
for record in d:
    print('{0[name]:12s}|{0[age]:4d}'.format(record))
```
```sh
$ python 4.py 
Yamada      | 123
Takahashi   |  88
```

##### アンパックによるキー参照

```python
d = [{'name': 'Yamada', 'age': 123}, {'name': 'Takahashi', 'age': 88}]
for r in d:
    print('{name:12s}|{age:4d}'.format(**r))
```
```sh
$ python 5.py 
Yamada      | 123
Takahashi   |  88
```

* format関数の引数がすっきりして見やすい
* フォーマットも余計な番号が消えて見やすい

もし辞書のキーをいちいち参照すると、以下のようにタイプ数が増える。

6.py
```python
d = [{'name': 'Yamada', 'age': 123}, {'name': 'Takahashi', 'age': 88}]
for r in d:
    print('{0:12s}|{1:4d}'.format(r['name'], r['age']))
```

> 全てのローカルな変数が入った辞書を返す組み込み関数 [vars()](https://docs.python.jp/3/library/functions.html#vars) と組み合わせると特に便利です。

> [str.format()](https://docs.python.jp/3/library/stdtypes.html#str.format) による文字列書式設定の完全な解説は、 [書式指定文字列の文法](https://docs.python.jp/3/library/string.html#formatstrings) を参照してください。

