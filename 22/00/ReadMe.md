# [9.8. イテレータ (iterator)](https://docs.python.jp/3/tutorial/classes.html#iterators)

< [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## ループできる

> for 文を使うとほとんどのコンテナオブジェクトにわたってループを行うことができます

```python
for element in [1, 2, 3]: print(element)
for element in (1, 2, 3): print(element)
for key in {'one':1, 'two':2}: print(key)
for char in "123": print(char)
for line in open("myfile.txt"): print(line, end='')
```

list, tuple, dict, string, fileobject。でもURLやファイルパスではできないと思う。

### 統一感？

> こういう要素へのアクセス方法は明確で簡潔で使い易いものです。イテレータの活用は Python へ広く行き渡り、統一感を持たせています。

しかし以下のように少し複雑なことをしようとすると同じようには書けない。しかも各関数の名前と挙動を記憶しておかねば書けない。

```python
for i, name in enumerate(['Yamada', 'Tanaka']): print(i, name)
```
```python
for k, v name in {'name':'Yamada', 'age':10}.items(): print(k, v)
```

### iter()

> 裏では for 文はコンテナオブジェクトに対して iter() 関数を呼んでいます。関数は、コンテナの中の要素に1つずつアクセスする __next__() メソッドが定義されているイテレータオブジェクトを返します。これ以上要素が無い場合は、 __next__() メソッドは StopIteration 例外を送出し、その通知を受け for ループは終了します。組み込みの next() 関数を使って __next__() メソッドを直接呼ぶこともできます; この例は関数がどう働くのかを示しています:

```python
s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
```
```sh
$ python 0.py 
<str_iterator object at 0xb7158c8c>
a
b
c
Traceback (most recent call last):
  File "0.py", line 7, in <module>
    print(next(it))
StopIteration
```

## 独自実装

> イテレータプロトコルの裏にある仕組みを観察していれば、自作のクラスにイテレータとしての振舞いを追加するのは簡単です。 __next__() メソッドを持つオブジェクトを返す __iter__() メソッドを定義するのです。クラスが __next__() メソッドを定義している場合、 __iter__() メソッドは単に self を返すことも可能です:

```python
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self): return self
    def __next__(self):
        if self.index == 0: raise StopIteration
        self.index -= 1
        return self.data[self.index]

if __name__ == '__main__':
    print('for --------')
    r = Reverse([1,2,3])
    print(r)
    for v in r:
        print(v)
    print('next() --------')
    r = Reverse([1,2,3])
    print(next(r))
    print(next(r))
    print(next(r))
    print(next(r))
```
```sh
$ python 1.py 
for --------
<__main__.Reverse object at 0xb714fdac>
3
2
1
next() --------
3
2
1
Traceback (most recent call last):
  File "1.py", line 22, in <module>
    print(next(r))
  File "1.py", line 7, in __next__
    if self.index == 0: raise StopIteration
StopIteration
```

for文でもnext()でもアクセスできた。next()で次がないと`StopIteration`例外が発生する。

よくわからないが、全てのクラスが継承するobjectに__iter__(), __next__()があるのだろうか？それをオーバーライドするから、組み込み関数のnext()で使える？

