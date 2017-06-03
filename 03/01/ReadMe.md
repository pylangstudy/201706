# [5.2. del 文](https://docs.python.jp/3/tutorial/datastructures.html#the-del-statement)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## del

### 指定インデックス

0.py
```python
l = [10,20,30,40,50]
del l[2]
print(l)
```
```python
$ python3 0.py
[10, 20, 40, 50]
```

インデックス`2`の要素が削除された。

### 指定範囲インデックス

```python
l = [10,20,30,40,50]
del l[1:3]
print(l)
```
```python
$ python3 1.py
[10, 40, 50]
```

### 全範囲

```python
l = [10,20,30,40,50]
del l[:]
print(l)
```
```python
$ python3 2.py
[]
```

### 指定変数

```python
l = [10,20,30,40,50]
del l
print(l)
```
```python
$ python3 3.py 
NameError: name 'l' is not defined
```

lにNoneが代入されるかと思いきや、lが未定義エラーになった。

### dictのキー削除

```python
l = {'key1': 'value1', 'key2': 'value2'}
del l['key1']
print(l)
```
```python
$ python3 4.py 
{'key2': 'value2'}
```

