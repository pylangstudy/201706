# [5.3. タプルとシーケンス](https://docs.python.jp/3/tutorial/datastructures.html#tuples-and-sequences)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## シーケンス

> リストや文字列には、インデクスやスライスを使った演算のように、数多くの共通の性質があることを見てきました。これらは シーケンス (sequence) データ型 ([シーケンス型 — list, tuple, range](https://docs.python.jp/3/library/stdtypes.html#typesseq) を参照) の二つの例です。 

* sequence
    * list
    * tuple
    * range
    * str

> Python はまだ進歩の過程にある言語なので、他のシーケンスデータ型が追加されるかもしれません。

## tuple

> 標準のシーケンス型はもう一つあります: タプル (tuple) 型です。
> タプルはコンマで区切られたいくつかの値からなります。

カンマ区切りなのはlistやrangeと同様。それよりも囲い文字が無いか、`()`であることがポイントである。

0.py
```python
t = 1, 2, 3
print(t)
for x in t:
    print(x)
```
```sh
$ python3 0.py 
(1, 2, 3)
1
2
3
```

### タプルを作るときは`()`で囲ったほうが無難

> タプルを書くときは必ずしも丸括弧で囲まなくてもいいですが、(タプルが大きな式の一部だった場合は) 丸括弧が必要な場合もあります。

1.py
```python
t = (1, 2, 3)
print(t)
for x in t:
    print(x)
```
```sh
$ python3 1.py 
(1, 2, 3)
1
2
3
```

### 代入不可

> タプルの要素を代入することはできません。

[immutable](https://docs.python.jp/3/glossary.html#term-immutable)である点がリストとは異なる。

```python
>>> t = (1,2,3)
>>> t[0] = 10
TypeError: 'tuple' object does not support item assignment
```

### リストとタプルの違い

項目|tuple|list
----|------|----
変更性|[immutable](https://docs.python.jp/3/glossary.html#term-immutable)|[mutable](https://docs.python.jp/3/glossary.html#term-mutable)
要素アクセス|インデックス、アンパック|イテレート
要素の型|違う場合も多い|たいてい同じ型

### 空タプルの生成

用途が思いつかないが。

```python
>>> t = ()
>>> len(t)
0
>>> for x in t:
...  t
... 
>>> 
```

### 要素が1個だけのタプル

#### NG

`t = (10)`とすればいいように思える。しかしこれはint型になってしまうらしい。

```python
>>> t = (10)
>>> len(t)
TypeError: object of type 'int' has no len()
```

タプルは`()`を外した形でも表現できるが、その場合は`t = 10`となってしまう。int型の値を代入した形になってしまう。

```python
>>> t = 10
>>> len(t)
TypeError: object of type 'int' has no len()
```

#### OK

`t = (10,)`のように末尾にカンマを付与することでタプル型として認識させることができる。

> 美しくはないけれども、効果的です。

というより、`()`を外した記法と整合性をとりつつ、int型代入との違いを作り出し、できるだけ短く書くための苦肉の策にみえる。美しいどころか、見づらさ、読みにくさ、わかりにくさにも一役買っている。しかし、そもそも1要素だけのタプルなど使い道があるのか不明なので、大した問題にはならないのだろう。

```python
>>> t = (10,)
>>> len(t)
1
```
```python
>>> t = 10,
>>> len(t)
1
```

### 代入

タプル型の代入式。「シーケンスのアンパック」とも呼ぶらしい。

```python
>>> x, y = (10, 20)
>>> print(x,y)
10 20
```

#### 右辺と左辺の要素数が同一であること

> シーケンスのアンパックでは、等号の左辺に列挙されている変数が、右辺のシーケンスの長さと同じ数だけあることが要求されます。

##### 左辺が1つだけだとタプルの代入になる

```python
>>> x = (10, 20)
>>> x
(10, 20)
```

##### 左辺が多いとエラー

```python
>>> x, y = (10,)
ValueError: need more than 1 value to unpack
```
```python
>>> x, y, z = (10, 20)
ValueError: need more than 2 values to unpack
```

##### 左辺が少ないとエラー

```python
>>> x, y = (10, 20, 30)
ValueError: too many values to unpack (expected 2)
```

#### 標準APIで使う

タプルのアンパック記法、C言語では悪習だと思う。可読性の低下につながるから。1行に複数の変数を宣言したり代入式を書くのでなく、複数行に分けるのが良いとされる。

しかし、Pythonではむしろ可読性を改善するために否応なしに使わざるを得ない場合があると思う。たとえばファイルの拡張子を取得する標準API [os.path.splitext](https://docs.python.jp/3/library/os.path.html#os.path.splitext) がある。このAPIはタプル型で値を返す。

```python
>>> import os.path
>>> root, ext = os.path.splitext('/tmp/some.py')
>>> print(root, ext)
/tmp/some .py
```

`/tmp/some`と`.py`の2つの要素をもったタプルとして返される。もし2つの変数名を宣言せねば、タプル型として返され、インデックス`[1]`を指定しないと拡張子が取得できない。変数名としてわかりにくくなる。この仕様はどうかと思う。

```python
>>> a = os.path.splitext('/tmp/some.py')
>>> a
('/tmp/some', '.py')
>>> a[1]
.py
```

いずれにせよ、タプルのアンパックは知らなくていいことではない。

