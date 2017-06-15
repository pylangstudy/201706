# [9.1. 名前とオブジェクトについて](https://docs.python.jp/3/tutorial/classes.html#a-word-about-names-and-objects)

[9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## オブジェクトの個体性

> オブジェクトには個体性があり、

ある名前がいつも特定のオブジェクトを指し示すことになる、という意味だろう。

## 別名付け(ailias)

> 同一のオブジェクトに(複数のスコープから) 複数の名前を割り当てることができます。この機能は他の言語では別名づけ(ailias) として知られています。

`alias`というスペルが正しいと思われる。「別名定義」や「エイリアス」という呼び名でよく聞く。

### ミュータブルな型にとっては効果的

> Python を一見しただけでは、別名づけの重要性は分からないことが多く、変更不能な基本型 (数値、文字列、タプル)を扱うときには無視して差し支えありません。

> しかしながら、別名付けは、リストや辞書や他の多くの型など、変更可能な型を扱う Python コード上で驚くべき効果があります。

「驚くべき効果があります」とは直感的でなく理解が難しいという意味だろうか。

### 参照渡し

> 別名付けはいくつかの点でポインタのように振舞い、このことは通常はプログラムに利するように使われます。例えば、オブジェクトの受け渡しは、実装上はポインタが渡されるだけなのでコストの低い操作になります。また、関数があるオブジェクトを引数として渡されたとき、関数の呼び出し側からオブジェクトに対する変更を見ることができます — これにより、 Pascal にあるような二つの引数渡し機構をもつ必要をなくしています。

なぜ別名定義が参照渡しの話になるのか謎。

文章から「Pythonには値渡しはない。参照渡ししかない」ということらしい。必要性については使い方次第だと思うが、値渡しがしたくても言語仕様上できないということだろう。引数を関数内部で変更してしまうと、呼出元の変数まで変えられてしまうということである。理解していないとバグの元になる。

「値渡しできない」ということを「二つの引数渡し機構をもつ必要をなくしています」という、さも利点であるかのように表現しているせいで読み取りにくい。例によって、このPython文書独特の「欠点を隠す」記述法である。それに対抗する「粗探し読法」に少し慣れてきた。

## コード

別名定義における具体的なコードが1つもなかった。これまでのコードを思い返して、それらしきものを考えると`as`のことを言っているのだと思う。

`datetime`に`d`という別名を定義する。
```python
import datetime as d
```

```python
>>> import datetime as d
>>> d.datetime.now()
datetime.datetime(2017, 6, 15, 8, 19, 52, 520868)
```

### 代入？

以下も`as`を使っているが、別名定義とは違う気がする。インスタンスや戻り値を変数に代入しただけに思える。

`open('a.txt')`の戻り値に`f`という別名を定義する。
```python
with open('a.txt') as f:
    print(f.read())
```
```python
try:
    raise Exception('エラー。')
except Exception as e:
    print(e)
```

### エラー

どういうわけか、`import datetime.datetime as d`はエラーになった。

```python
>>> import datetime.datetime as d
Traceback (most recent call last):
  File "<frozen importlib._bootstrap>", line 2218, in _find_and_load_unlocked
AttributeError: 'module' object has no attribute '__path__'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'datetime.datetime'; 'datetime' is not a package
```

エラーを見てみる。さっぱりわからない。

* 「別名定義できるのはパッケージだけ」ということか？
    * 今回は「オブジェクトの別名定義」についての話題だったと思うが？
        * モジュールはオブジェクトでなくPythonファイルのことではなかったのか？
        * パッケージはオブジェクトなのか？
        * パッケージはクラスなのか？
        * そもそも、オブジェクト、class, type, パッケージ、モジュールとは何か？
    * 「datetime.datetime」はパッケージ？モジュール？クラス？
        * 「datetime.datetime」はクラスだと思う
            * クラスは別名定義できないということか？
            * クラスはimportできないということか？

「モジュールはPythonファイルのことである」というこれまでの教えも怪しくなってきた。

> このファイルを モジュール (module) と呼びます。

https://docs.python.jp/3/tutorial/modules.html

### importしたものの型を調べる

```python
>>> import os.path as p
>>> p.isfile('a.txt')
False
>>> type(p)
<class 'module'>
```
```python
>>> import datetime as d
>>> type(d)
<class 'module'>
>>> type(d.datetime)
<class 'type'>
```

名前|type()|別名定義できたか
----|------|---------------
`os.path`|`<class 'module'>`|○
`datetime`|`<class 'module'>`|○
`datetime.datetime`|`<class 'type'>`|✗

これを見る限りでは、「別名定義できるのはmoduleだけである。型(type)はできない」ということになる。よく見ると`<class 'module'>`とある。モジュールはimportされると`class`になるのか？classとtypeの違いは？さっぱりわからない。

### datetime.datetimeの正体

`datetime.datetime`はクラスである。

http://www.lifewithpython.com/2014/07/python-get-location-of-libraries-modules-packages.html

```python
>>> import datetime
>>> datetime.__file__
'/home/{user}/.pyenv/versions/3.6.1/lib/python3.6/datetime.py'
```

「datetime.py」というファイルが「datetime」というモジュールになる。そのファイル内で`class datetime(date):`という定義があった。これが「datetime」というクラスを指しているのだろう。`datetime.datetime`はクラスだった。

### `import datetime.datetime`でエラーになる理由

importできるのはモジュールだけだから。クラスである`datetime.datetime`はimportできない。

ただし、`from datetime import datetime`なら可能。

```python
>>> from datetime import datetime as d
>>> d.now()
datetime.datetime(2017, 6, 15, 8, 59, 0, 624701)
```

1. datetimeモジュールから
1. datetimeクラスを取り込む
1. datetimeクラスに`d`という別名定義をする
1. クラス`d`のクラスメソッド`now()`を呼び出す

これでクラスも取り込め、クラスに別名定義ができた。`from ... import ...`の意味、datetimeモジュールとクラスについて理解している必要がある。

#### now()

ついでに、いつも使う`now()`関数を探してみた。

```python
@classmethod
def now(cls, tz=None):``
```

クラスメソッドらしい。`dateitme.datetime.now()`という呼出ができるのも納得。datetimeインスタンスを生成せず、クラス名から直接呼出ができるのはクラスメソッドだからだった。

## まとめ

* Pythonは別名定義ができる
    * モジュール: `import datetime as d`
    * クラス: `from datetime import datetime as d`
* Pythonはすべて参照渡しである。値渡しはできない

### 謎

* なぜ「名前とオブジェクト」で「参照渡しのみ。値渡しできない」という話題がでたのか？別名定義の機構と関係あるのか？
* moduleとはPythonコードが書かれたファイルではなかったのか？
    * `type(os.path)`で`<class 'module'>`と出力される
        * モジュールは取り込まれるとclassとして扱われる？
            * モジュール、パッケージ、class、typeに対する理解ができていない？
