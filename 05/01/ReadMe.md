# [5.5. 辞書型 (dictionary)](https://docs.python.jp/3/tutorial/datastructures.html#dictionaries)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 辞書(dict)

> 辞書は他の言語にも “連想記憶 (associated memory)” や “連想配列 (associative array)” という名前で存在することがあります。
> 辞書は キー (key) でインデクス化されています。

* キー重複なし
    * キーは一意である
        * キー値は上書きされる
* キー順序なし
* キーは変更不能
    * キーにできるのは文字列、数値型、それを含むタプルのみ
    * 変更可能な型はキーにできない(list等)
* `blank_dict = {}`
* `some_dict = {'key1': 'value1', 'key2': 'value2'}`

### 空の辞書

```python
blank_dict = {}
print(blank_dict)
```
```sh
$ python3 0.py 
{}
```

### 任意の辞書

### `{k:v}`

```python
some_dict = {'key1': 'value1', 'key2': 'value2'}
print(some_dict)
```
```sh
$ python3 1.py 
{'key1': 'value1', 'key2': 'value2'}
```

### コンストラクタ`dict(k=v)`

```python
d = dict(key1='value1', key2='value2', key3='value3')
print(d)
```
```sh
$ python3 8.py 
{'key3': 'value3', 'key1': 'value1', 'key2': 'value2'}
```

### コンストラクタ`dict([(k,v)])`

```python
d = dict( [('key1', 'value1'), ('key2', 'value2')] )
print(d)
```
```sh
$ python3 5.py 
{'key2': 'value2', 'key1': 'value1'}
```

### 追加と変更

```python
some_dict = {}
print(some_dict)
some_dict['key1'] = 'value1'    # keyが存在しなければ新規追加
print(some_dict)
some_dict['key1'] = 'value111'  # keyが存在すれば値の上書き
print(some_dict)
```
```sh
$ python3 2.py 
{}
{'key1': 'value1'}
{'key1': 'value111'}
```

### キーの包含確認

```python
some_dict = {'key1': 'value1', 'key2': 'value2'}
print('key1' in some_dict)
print('key100' in some_dict)
```
```sh
$ python3 3.py 
True
False
```

### キーの削除

```python
some_dict = {'key1': 'value1', 'key2': 'value2'}
print(some_dict)
del some_dict['key1']
print(some_dict)
```
```sh
$ python3 4.py
{'key1': 'value1', 'key2': 'value2'}
{'key2': 'value2'}
```

### キーの並べ替え

```python
some_dict = {'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}
print(sorted(some_dict.keys()))
```
```sh
$ python3 6.py 
['key1', 'key2', 'key3']
```

### キーによる値の並べ替え

```python
some_dict = {'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}
print([some_dict[key] for key in sorted(some_dict.keys())])
```
```sh
$ python3 7.py 
['value1', 'value2', 'value3']
```

### 辞書内包表記 (dict内包表記)

```python
d = {x: x**2 for x in range(5)}
print(d)
```
```sh
$ python3 9.py 
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

* [リスト内包表記](https://docs.python.jp/3/tutorial/datastructures.html#list-comprehensions) `[x for x in iterable]`
* [セット内包表記](https://docs.python.jp/3/tutorial/datastructures.html#sets) `{x for x in iterable}`
* [辞書内包表記](https://docs.python.jp/3/tutorial/datastructures.html#list-comprehensions) `{x: x for x in iterable}`

セットと辞書が同じ記号を使うため見分けにくい。

Pythonは読みやすさより、短く書けることに注力しているように思える。

