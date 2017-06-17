# [9.3.2. クラスオブジェクト](https://docs.python.jp/3/tutorial/classes.html#class-objects)

< [9.3. クラス初見](https://docs.python.jp/3/tutorial/classes.html#a-first-look-at-classes) < [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

> クラス・オブジェクトでは２種類の演算、属性参照とインスタンス生成をサポートしています。

## 属性参照

> 属性参照 (attribute reference) は、Python におけるすべての属性参照で使われている標準的な構文、 obj.name を使います。

> クラスオブジェクトが生成された際にクラスの名前空間にあった名前すべてが有効な属性名です。

```python
class MyClass:
    var = 'my_class_var'
    def func():
        print('func()')

print(MyClass.var)
MyClass.func()

MyClass.var = 'after'
print(MyClass.var)
```
```sh
$ python3 0.py 
my_class_var
func()
after
```

### __doc__

```python
class MyClass:
    """MyClass docs.

some description."""
    pass

print(MyClass.__doc__)
```
```sh
$ python3 1.py 
MyClass docs.

some description.
```

先頭に`__`がつくとプライベート変数になり、`インスタンス._クラス名__プライベート変数名`という書式でないと参照できなくなるはず。なのに`__doc__`はその名前のまま参照できている。`__doc__`は特殊な扱いなのか？

### インスタンス生成

> クラスの インスタンス化 (instantiation) には関数のような表記法を使います。

```python
インスタンス変数名 = クラス名()
```
```python
c = MyClass()
```

> クラスオブジェクトのことを、単にクラスの新しいインスタンスを返す引数がない関数のように振る舞います。

日本語が変。「MyClassというクラスオブジェクトは、そのクラスのインスタンスを返す関数として振舞う」と言っているのか？

### `c = MyClass()`は空のオブジェクトを返す？

> このクラスのインスタンス生成操作 (クラスオブジェクトの “呼出し”) を行うと、空のオブジェクトを生成します。

以下のような疑問を抱く。

* 空のオブジェクトとは何か？
* `var`, `func`の名前を持ったオブジェクトではないのか？

```python
class MyClass:
    var = 'my_class_var'
    def func():
        print('func()')

c = MyClass()
print(c.var)
c.func()
```
```sh
$ python3 2.py 
my_class_var
Traceback (most recent call last):
  File "2.py", line 8, in <module>
    c.func()
TypeError: func() takes 0 positional arguments but 1 was given
```

実行するとエラーになる。「`c.func()`は0の位置引数をとるが、1が与えられた」みたいなエラー。意味不明である。Python文書で後述されると思うが、インスタンスから参照するときはインスタンスメソッドの形式にする必要がある。第一引数に`self`が必要である。`def func(self):`とすることで解決する。呼出時に引数は不要。

### コンストラクタ

> 多くのクラスは、オブジェクトを作成する際に、カスタマイズされた特定の初期状態になってほしいと望んでいます。そのために、クラスには __init__() という名前の特別なメソッド定義することができます。

```python
class MyClass:
    def __init__(self):
        self.var = 'var_init'

c = MyClass()
print(c.var)
```
```sh
$ python3 3.py 
var_init
```

`__init__()`メソッドは自動的に実行される。インスタンス生成時(`c = MyClass()`)に。

#### 引数あり

```python
class Human:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age

c = Human('Yamada')
print(c.name)
print(c.age)
```
```sh
$ python3 4.py 
Yamada
10
```

