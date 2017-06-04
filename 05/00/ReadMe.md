# [5.4. 集合型](https://docs.python.jp/3/tutorial/datastructures.html#sets)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 集合(set)

* 重複なし
* 順序なし
* `blank_set = set()`
* `some_set = {'a', 'b'}`

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
```
```sh
$ python3 0.py 
{'banana', 'orange', 'apple', 'pear'}
```

### `{}`

`{}`で囲うのは辞書(dict)型変数と同じ記法である。`d = {}`とすると空の辞書が生成される。空の集合は`s = set()`とする。

### `set()`は関数ではなくコンストラクタでは？

> [set()](https://docs.python.jp/3/library/stdtypes.html#set) 関数は set を生成するために使用することができます。

とあるが、リンク先には`setオブジェクト`や`class set([iterable])`という表記があることからコンストラクタと思われる。

### mutableである

集合はmutableである。

```python
basket = set()
print(basket)
basket.add('apple')
print(basket)
basket.add('apple')
print(basket)
basket.update({'orange', 'banana'})
print(basket)
```
```sh
$ python3 1.py 
set()
{'apple'}
{'apple'}
{'orange', 'banana', 'apple'}
```

### 包含確認

```python
basket = {'apple', 'orange', 'banana'}
print('apple' in basket)
print('kkkk' in basket)
```
```sh
$ python3 2.py 
True
False
```

### 演算

> Set オブジェクトは、和 (union)、積 (intersection)、差 (difference)、対称差 (symmetric difference)といった数学的な演算もサポートしています。

```python
a = {'A', 'B', 'C'}
b = {'D', 'E', 'A'}
print('a =', a)
print('b =', b)
print('a - b =', a - b) # 差
print('b - a =', b - a) # 差
print('a | b =', a | b) # 和
print('a & b =', a & b) # 積
print('a ^ b =', a ^ b) # 対称差
```
```sh
$ python3 3.py 
a = {'A', 'B', 'C'}
b = {'A', 'D', 'E'}
a - b = {'B', 'C'}
b - a = {'D', 'E'}
a | b = {'B', 'C', 'A', 'D', 'E'}
a & b = {'A'}
a ^ b = {'D', 'B', 'E', 'C'}
(a | b) - (a & b) = {'E', 'B', 'C', 'D'}
```

演算子|演算|説明
------|----|----
`-`|差|片方の集合に存在する要素のみを持った部分集合を得る（共通要素の削除）
`|`|和|両方の集合に存在する要素を合わせた集合を得る
`&`|積|両方の集合に存在する要素のみを持った集合を得る（差異要素の削除）
`^`|対称差|和から積を省いた集合を得る


### set内包表記（集合内包表記）

[list内包表記](https://github.com/pylangstudy/201706/blob/master/01/01/ReadMe.md)のset版。

#### 文字列シーケンス

```python
a = {x for x in 'ABCD' if x not in 'AB'}
print(a)
```
```sh
$ python3 4.py 
{'C', 'D'}
```

#### 集合

```python
a = {x for x in {'A', 'B', 'C', 'D'} if x not in {'A', 'B'}}
print(a)
```
```sh
$ python3 5.py 
{'D', 'C'}
```

#### 集合（独自クラス）

```python
class MyClass:
    def __init__(self, name):
        self.__name = name
    def Show(self):
        print(self.__name)
c1 = MyClass('c1')
c2 = MyClass('c2')
c3 = MyClass('c3')
c4 = MyClass('c4')
a = {x.Show() for x in {c1, c2, c3, c4} if x not in {c1, c2}}
```
```sh
$ python3 6.py 
c4
c3
```

