# [5.1.4. ネストしたリストの内包表記](https://docs.python.jp/3/tutorial/datastructures.html#nested-list-comprehensions)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## ネスト

0.py
```python
matrix = [[1,2,3],[4,5,6]]
print([[row[i] for row in matrix] for i in range(3)])
```
```python
$ python3 0.py
[[1, 4], [2, 5], [3, 6]]
```

以下の文と等価という。最も外側のリスト内包表記を解く。

1.py
```python
matrix = [[1,2,3],[4,5,6]]
result = []
for i in range(3):
    result.append([row[i] for row in matrix])
print(result)
```
```python
$ python3 1.py
[[1, 4], [2, 5], [3, 6]]
```

さらにネストしたリスト内包表記を解く。

2.py
```python
matrix = [[1,2,3],[4,5,6]]
result = []
for i in range(3):
    result_row = []
    for row in matrix:
        result_row.append(row[i])
    result.append(result_row)
print(result)
```
```python
$ python3 2.py
[[1, 4], [2, 5], [3, 6]]
```

### おさらい

#### リスト内包表記

```python
>>> [row for row in matrix]
[[1, 2, 3], [4, 5, 6]]
```
```python
>>> [i for i in range(3)]
[0, 1, 2]
```

#### リスト内包表記における連続したfor文

```python
>>> [row[i] for row in matrix for i in range(3)]
[1, 2, 3, 4, 5, 6]
```
これも普通にfor文をネストした以下と同じ。
```python
matrix = [[1,2,3],[4,5,6]]
for row in matrix:
    for i in range(3):
        print(row[i])
```
左から順にネストしたfor文と同義のためわかりやすかった。しかし、ネストしたリスト内包表記は違う。

### ネスト時の順序

> ネストしたリスト内包表記は、続く for のコンテキストの中で評価されます。

という点がポイント。

```python
>>> matrix = [[1,2,3],[4,5,6]]
>>> [[row[i] for row in matrix] for i in range(3)]
[[1, 4], [2, 5], [3, 6]]
```
以下の順になるらしい。左から順ではない。
```python
>>> for i in range(3):
...     [row[i] for row in matrix]
... 
[1, 4]
[2, 5]
[3, 6]
```

> 前の節で見たように、

と言っているが、前節にそんな記述あったか？ネストについてはこの節ではじめて触れたように見えるが。ネストしていない時は左から順でわかりやすかったのに。

#### リスト内包表記

文書には明記されていないと思うが、リスト内包表記の構文は以下のはず。

```python
[式 for item in iterable]
```

「式は最後に評価される」ということか。それを直接書いてはいなかったが、実行するとそのように動作している。リスト内包表記のルールを以下にまとめる。

* リスト内包表記の構文は`[式 for item in iterable]`である
* `式`は最後に評価される
* `式`にはリスト内包表記を指定できる（ネストできる）

ところで、iterable にはリスト内包表記をネストできないのか？

#### iterableにリスト内包表記をネストしてみる

```python
>>> [x*2 for x in [i+1 for i in range(5)]]
[2, 4, 6, 8, 10]
```

1. `range(5)`で`[0,1,2,3,4]`ができる
1. `i+1`で`0+1, 1+1, 2+1, 3+1, 4+1`される
1. `[... for ... in ...]`でリスト(`[1,2,3,4,5]`)になる
1. `[x*2 for x in [1,2,3,4,5]]`で`1*2, 2*2, 3*2, 4*2, 5*2`される
1. `[... for ... in ...]`でリスト(`[2,4,6,8,10]`)になる

できた。

#### 式とiterableにリスト内包表記をネストしてみる

```python
>>> [[x+j for x in [10,20]] for j in [i+1 for i in range(5)]]
[[11, 21], [12, 22], [13, 23], [14, 24], [15, 25]]
```

ものすごく見づらくわかりにくい。ネスト表記を一つずつ外してみる。

```python
>>> for i in range(5):
...     j = i+1
...     [x+j for x in [10,20]]
... 
[11, 21]
[12, 22]
[13, 23]
[14, 24]
[15, 25]
```

* リスト内包表記の構文は`[式 for item in iterable]`である
* 式は最後に実行される。iterableのほうが先。`[x+j for x in [10,20]]`より`[[i+1 for i in range(5)]]`が先。

```python
>>> for i in range(5):
...     j = i+1
...     for x in [10,20]:
...         x+j
... 
11
21
12
22
13
23
14
24
15
25
```

### forの直後に式は指定できない

for のすぐ後ろに式を指定すると`SyntaxError`になる。

```python
>>> [[x+j for x in [100,200]] for j+10 in [i+1 for i in range(5)]]
  File "<stdin>", line 1
SyntaxError: can't assign to operator
```

リスト内包表記だけかと思いきや、for文でも同様。
```python
>>> for a+1 in range(5):
...  print(a)
... 
  File "<stdin>", line 1
SyntaxError: can't assign to operator
```

* 「forの直後には変数の宣言しかできない」のだろう。たぶん。

## まとめ

### for文

```python
for 変数名 in iterable:
    文
```

### リスト内包表記

```python
[式 for item in iterable]
```

#### 連続したfor文

```python
[式 for i in iterable for j in iterable ]
```

#### if文

```python
[式 for i in iterable if 条件式]
```

### リスト内包表記のネスト

#### 式でネスト

```python
[[row[i] for row in matrix] for i in range(3)]
```

#### iterableでネスト

```python
[x*2 for x in [i+1 for i in range(5)]]
```

#### 式とiterableでネスト

```python
[[x+j for x in [10,20]] for j in [i+1 for i in range(5)]]
```

