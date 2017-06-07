# [5.8. シーケンスとその他の型の比較](https://docs.python.jp/3/tutorial/datastructures.html#comparing-sequences-and-other-types)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## シーケンス同士の比較

> シーケンスオブジェクトは同じシーケンス型の他のオブジェクトと比較できます。

```python
>>> [1,2,3] == [1,2,3]
True
>>> [1,2] == [1,3]
False
```

### 文字列シーケンス

> 比較には 辞書的な (lexicographical) 順序が用いられます。

```python
>>> "ABC" < "ABD"
True
>>> "ABC" > "ABD"
False
```

> 最初の二つの要素を比較し、その値が等しくなければその時点で比較結果が決まります。等しければ次の二つの要素を比較し、以降シーケンスの要素が尽きるまで続けます。比較しようとする二つの要素がいずれも同じシーケンス型であれば、そのシーケンス間での辞書比較を再帰的に行います。二つのシーケンスの全ての要素の比較結果が等しくなれば、シーケンスは等しいとみなされます。片方のシーケンスがもう一方の先頭部分にあたる部分シーケンスならば、短い方のシーケンスが小さいシーケンスとみなされます。文字列に対する辞書的な順序づけには、個々の文字を並べるのに Unicode コードポイントの数を用います。

上記の文はわかりにくいが、おそらく以下のように「両者を先頭から1文字ずつ比較する」と言っているのだろう。

```python
>>> [x for x in zip("ABC","ABD")]
[('A', 'A'), ('B', 'B'), ('C', 'D')]
```

差異が出るのは3文字目。`C`と`D`。Cのほうが小さいため`"ABC" < "ABD"`は`True`となる。`C`と`D`のUnicodeコードポイントはそれぞれ`U+0043`と`U+0044`。`0x43 < 0x44`なので`C < D`

https://ja.wikipedia.org/wiki/Unicode%E4%B8%80%E8%A6%A7_0000-0FFF

### 先頭から順に比較する

```python
>>> (1,2) < (1,3)
True
>>> (1,2) < (1,2,3)
True
>>> (1,2,3) < (1,3)
True
```

* 要素は先頭インデックスから順に比較する
    * 差異が出た時点で結果を返す
        * 対象インデックスの要素が存在しない場合、存在する側より小さいと判断される

#### ○: 異なる数値型

比較できる。

> 違う型のオブジェクト同士を < や > で比較することも、それらのオブジェクトが適切な比較メソッドを提供しているのであれば許可されます。

> 例えば、異なる数値型同士の比較では、その数値によって比較が行われます。例えば、 0 と 0.0 は等価です。

```python
>>> 0 == 0.0
True
>>> 0 < 0.1
True
>>> 0 > 0.1
False
```

整数型(int)、浮動小数点型(float)は型が異なるが比較できる。比較メソッドが提供されているらしい。

### ✗: 数値型と文字列型

> 一方、適切な比較順序がない場合は、インタープリターは TypeError 例外を発生させます。

```python
>>> 123 < '124'
TypeError: unorderable types: int() < str()
```

```python
>>> 123 == '123'
False
```

等式はエラーにならないらしい。

### ✗: 異なるシーケンス型同士

比較できない。

Python3.4.3
```python
>>> (1,2,3) < [1,2,4]
TypeError: unorderable types: tuple() < list()
```

Python3.6.1
```python
>>> (1,2,3) < [1,2,4]
TypeError: '<' not supported between instances of 'tuple' and 'list'
```

両バージョン
```python
>>> (1,2) == [1,2]
False
```

