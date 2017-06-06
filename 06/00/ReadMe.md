# [5.6. ループのテクニック](https://docs.python.jp/3/tutorial/datastructures.html#looping-techniques)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## `dict.items()`

辞書の全キーと値を展開する。

```python
d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for k, v in d.items():
    print(k, v)
```
```sh
$ python3 0.py
key3 value3
key1 value1
key2 value2
```

## `enumerate()`

リストの要素だけでなくインデックスも欲しいときに。

```python
l = ['a', 'b', 'c']
for i, item in enumerate(l):
    print(i, item)
```
```sh
$ python3 1.py
0 a
1 b
2 c
```

## `zip()`

> 各要素をひと組みにすることができます。

行列の入れ替え。

```python
l = ['a', 'b', 'c']
t = ('d', 'e', 'f')
r = range(3)
for item in zip(l, t, r):
    print(item)
```
```sh
$ python3 2.py
('a', 'd', 0)
('b', 'e', 1)
('c', 'f', 2)
```

## `reversed()`

```python
l = ['a', 'b', 'c']
for item in reversed(l):
    print(item)
```
```sh
$ python3 3.py
c
b
a
```

```python
for item in reversed(range(5)):
    print(item)
```
```sh
$ python3 4.py
4
3
2
1
0
```


## `sorted()`

### 集合

```python
l = ['C', 'B', 'A', 'A']
for item in sorted(set(l)):
    print(item)
```
```sh
$ python3 5.py
A
B
C
```
`set()`でリストを集合型(重複なし)にして、`sorted()`で昇順ソートする。

### 辞書

キーでソートと、値でソートした。

```python
d = {'Key3': 'A', 'Key2': 'B', 'Key1': 'C'}
for key in sorted(d.keys()):
    print(key, d[key])
for value in sorted(d.values()):
    print(value, [k for k,v in d.items() if value == v][0])
```
```sh
$ python3 6.py
Key1 C
Key2 B
Key3 A
A Key3
B Key2
C Key1
```

## ループ中に対象リストを変更しないほうが安全

> ときどきループ内でリストを変更したい誘惑に駆られるでしょうが、代わりに新しいリストを作ってしまうほうがより簡単で安全なことが、ままあります

### 毎回増やすと無限ループしてしまう

```python
l = [100, 200, 300]
for i, item in enumerate(l):
#    l.append(0) # 無限ループになる
    print(item)
```
```sh
$ python3 7.py
100
200
300
```

for対象のリストをループ中でappendすると無限ループになる。

### 削除するとループ数が減ってしまう

```python
l = [100, 200, None, 300]
for i, item in enumerate(l):
    if None is item:
        del l[i]
        continue
    print(item)
```
```sh
$ python3 8.py
100
200
```

`300`までループして欲しかったのに。

### 挿入すると参照位置がずれてしまう

```python
l = [100, 200, 300]
for i, item in enumerate(l):
    if i == 0: l.insert(0, 10)
    print(i, item)
print(l)
```
```
$ python3 9.py
0 100
1 100
2 200
3 300
[10, 100, 200, 300]
```
初回のみ`10`を追加して表示しようとしている。しかし実際は`100`が表示される。

### 解決

ループ対象リストとは別の新しい変数を用意することで解決する。

毎回要素を追加しても無限ループにならない。
```python
l = [100, 200, 300]
res = []
for i, item in enumerate(l):
    res.append(item)
    res.append(0)
print(res)
```
```sh
python3 A.py
[100, 0, 200, 0, 300, 0]
```

None要素を省いてもすべて参照できる。
```python
l = [100, 200, None, 300]
res = []
for i, item in enumerate(l):
    if None is not item: res.append(item)
print(res)
```
```sh
python3 B.py
[100, 200, 300]
```

挿入しても参照位置がずれない。
```python
l = [100, 200, 300]
res = []
for i, item in enumerate(l):
    if i == 0: res.insert(0, 10)
    res.append(item)
print(res)
```
```sh
$ python3 C.py
[10, 100, 200, 300]
```

