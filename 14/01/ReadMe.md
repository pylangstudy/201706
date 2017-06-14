# [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes)

< [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

一気に難しくなる。Pythonにおけるクラスの概念を把握するのがむずかしい。

## Modula-3

> Python のクラスは、C++ と Modula-3 のクラスメカニズムを混ぜたものです。

[Modula-3](https://ja.wikipedia.org/wiki/Modula-3)言語とは何か。Wikipediaにもほとんど情報がない。1980年代に作られたことから古いことだけは分かる。

## 矛盾した嘘の説明文

> Python は、他のプログラミング言語と比較して、最小限の構文と意味付けを使ってクラスを言語に追加しています。Python のクラスは、C++ と Modula-3 のクラスメカニズムを混ぜたものです。Python のクラス機構はオブジェクト指向プログラミングの標準的な機能を全て提供しています。

矛盾していると思う。

```
「最小限の構文と意味付け」≠「オブジェクト指向プログラミングの標準的な機能を全て提供しています」
```

少なくともカプセル化ができないことは知っている。

### カプセル化できない

オブジェクト指向のキモは「カプセル化」らしい。

http://qiita.com/tutinoco/items/6952b01e5fc38914ec4e

しかし、Pythonはカプセル化できない。

```python
class MyClass:
    def __init__(self):
        self.__private = 'private'
        self.public = 'public'

if __name__ == '__main__':
    c = MyClass()
    print(c.public)
#    print(c.__private) # AttributeError: 'MyClass' object has no attribute '__private'
    print(c._MyClass__private)
```

`self.__{任意の変数名}`のように、変数名の先頭に`__`を付与するとprivate的にできる。`{インスタンス}.__{変数名}`とすると`AttributeError`となり参照できない。カプセル化できているかに見える。しかし、`{インスタンス}._{クラス名}__{任意の変数名}`とすると参照できてしまう。カプセル化できないので「オブジェクト指向プログラミングの標準的な機能を全て提供しています」とは言えないと思う。

具体的に言うと、他の言語では`public`, `private`, `protected`, `internal`のアクセス修飾子があるが、Pythonでは事実上、`public`のみである。

#### オブジェクト指向？

そもそもカプセル化できないのに「オブジェクト指向」として成り立つのか？オブジェクト指向の定義も知らない私には判別不能。

#### 根拠

> Python のクラス機構はオブジェクト指向プログラミングの標準的な機能を全て提供しています。

という文章には、その根拠なのか以下の文が続く。

* ○: クラスの継承メカニズムは、複数の基底クラスを持つことができ、派生クラスで基底クラスの任意のメソッドをオーバライドすることができます
    * ？: メソッドでは、基底クラスのメソッドを同じ名前で呼び出すことができます
    * ○: オブジェクトには任意の種類と数のデータを格納することができます
* ✗: モジュールと同じく、クラス機構も Python の動的な性質に従うように設計されています
    * ✗: クラスは実行時に生成され、生成後に変更することができます。

オブジェクト指向についてよく知らないが、「✗」のせいでカプセル化できなくなるのだと思う。

また、「？」は`super().base_method()`のように呼び出すことになる。重要なのは、他のオブジェクト指向に存在するアクセス修飾子、`protected`が存在しない点である。先述の通り、Pythonには`public`しか存在しない。publicだから呼び出せて当たり前。「オブジェクト指向プログラミングの機能」というよりふつうにモジュールから関数を呼び出すのと同じだと言っているだけに見える。

「○」について不審な点はない。ただ、「オーバーロード」はできない。最新版でデコレータを駆使すればできるかのような話をチラッと見たことがあるが、よく知らない。

##### protectedがない

```python
class MyParent:
    def __init__(self):
        self.__private = 'private'
        self.public = 'public'
    
class MyChild(MyParent):
    def __init__(self):
        super().__init__()
    def Show(self):
        print(self.public)
        # protectedで子クラスにだけ参照させることができない。
#        print(self.__private) # AttributeError: 'MyChild' object has no attribute '_MyChild__private'
#        print(self._MyClass__private) # AttributeError: 'MyChild' object has no attribute '_MyChild__private'
#        print(super().__private) # AttributeError: 'super' object has no attribute '_MyChild__private'
#        print(super()._MyClass__private) # AttributeError: 'super' object has no attribute '_MyClass__private'

if __name__ == '__main__':
    cc = MyChild()
    cc.Show()
```
```sh
$ python3 1.py 
public
```

### 親クラスのメソッドを呼び出せる

```python
class MyParent:
    def parent_method(self):
        print('base_method')
class MyChild(MyParent):
    def child_method(self):
        print('child_method call: ', end='')
        self.parent_method()

if __name__ == '__main__':
    c = MyChild()
    c.parent_method()
    c.child_method()
```
```sh
$ python3 2.py 
base_method
child_method call: base_method
```

子クラスからは`self.{親クラスメソッド名}()`で呼び出せる。実行側は`{子クラスのインスタンス}.{親クラスメソッド名}`で呼び出せる。

### オーバーライドできる

```python
class MyParent:
    def parent_method(self):
        print('base_method')
class MyChild(MyParent):
    def parent_method(self):
        print('child_method call: ', end='')
        super().parent_method()
        # selfで呼び出すとMyChild.parent_methodが呼び出されて無限再帰してしまう。
#        self.parent_method() # RuntimeError: maximum recursion depth exceeded while calling a Python object

if __name__ == '__main__':
    c = MyChild()
    c.parent_method()
```
```sh
$ python3 3.py 
child_method call: base_method
```

子が親と同名のメソッドを定義すると上書きされる。子メソッド側で親メソッドを呼び出したいときは`super()`から呼び出せる。しかし、`MyChild()`のインスタンスからは`MyParent.parent_method()`を直接呼び出すことはできない。

### インスタンス生成後に改変する

```python
class MyClass:
    def my_method(self):
        print('base_method')

if __name__ == '__main__':
    c = MyClass()
    c.new_method = lambda: print('new_method')
    c.new_method()
```
```sh
$ python3 4.py 
new_method
```

なんと、インスタンス生成後に新しいメソッドを追加できてしまえる。もはや「型」と言えるのかも不明。カプセル化できないどころか、追加できてしまう。

#### privateの追加

```python
class MyClass:
    def my_method(self):
        print('base_method')

if __name__ == '__main__':
    c = MyClass()
    c.new_public = 'new_public'
    print(c.new_public)
    
#    c.__new_private = 'new_private'
#    print(c.__new_private) # AttributeError: 'MyClass' object has no attribute '_MyClass__new_private'
#    print(c._MyClass__new_private) # AttributeError: 'MyClass' object has no attribute '_MyClass__new_private'

    c._MyClass__new_private = 'new_private'
    print(c._MyClass__new_private)
#    print(c.__new_private) # AttributeError: 'MyClass' object has no attribute '__new_private'
```
```sh
$ python3 5.py 
new_public
new_private
```
private変数も追加できた。privateでも何でもないが。

## Pythonはprivateにできない

> C++ の用語で言えば、通常のクラスメンバ (データメンバも含む) は ([プライベート変数](https://docs.python.jp/3/tutorial/classes.html#tut-private) に書かれている例外を除いて) public であり、メンバ関数はすべて 仮想関数(virtual) です。 

[プライベート変数](https://docs.python.jp/3/tutorial/classes.html#tut-private)のリンク先をみても、第一声で自身のタイトルを否定している。

> オブジェクトの中からしかアクセス出来ない “プライベート” インスタンス変数は、 Python にはありません。

この時点で、以下の文は間違いとなる。

> ([プライベート変数](https://docs.python.jp/3/tutorial/classes.html#tut-private) に書かれている例外を除いて) public であり、

「Pythonにはプライベート変数はない。すべてpublicである」が正しい。

## self

> メソッド関数の宣言では、オブジェクト自体を表す第一引数を明示しなければなりません。

インスタンスメソッドには必ず`self`が必要。

```python
class MyClass:
    class_var = 'class_var'
    def __init__(self):
        self.instance_var = 'instance_var'
    def instance_method(self):
        print('instance_method:', self.instance_var)
        print('instance_method:', self.class_var)
#        print(class_var) # NameError: name 'class_var' is not defined
    @classmethod
    def class_method(cls):
        print('class_method:', cls.class_var)
#        print('class_method:', cls.instance_var) # AttributeError: type object 'MyClass' has no attribute 'instance_var'
    @staticmethod
    def static_method():
        print('static_method')
#        print('static_method: ', class_var) # NameError: name 'class_var' is not defined
#        print('static_method: ', instance_var) # NameError: name 'instance_var' is not defined

if __name__ == '__main__':
    c = MyClass()
    c.instance_method()
    c.class_method()
    MyClass.static_method()
```
```sh
$ python3 6.py 
instance_method: instance_var
instance_method: class_var
class_method: class_var
static_method
```

## 用語

### メソッドと関数

「メソッド関数」という言葉が謎である。メソッドと関数は以下のように呼び分けていると思っている。

名前|説明
----|----
関数|モジュール配下にあるdef定義。
メソッド|class配下にあるdef定義。

文言の統一くらいして欲しい。混乱するから。まとめておく。

名前|説明
----|----
関数(Python用語)|モジュール配下にあるdef定義。
メソッド(Python用語)|class配下にあるdef定義。
メソッド関数|そんな言葉は知らない。
メンバ関数(C++用語)|メソッドのこと。
仮想関数(C++用語)|派生クラスで再定義されるメンバー関数のこと。
純粋仮想関数(C++用語)|実装のない関数。別言語では「抽象メソッド」という

## クラス、インスタンス、オブジェクト

名前|説明
----|----
クラス|`class MyClass:`のように定義したもの。
クラスインスタンス|`c = MyClass()`で代入されたもの。
オブジェクト|すべてのクラスの継承元。

クラスインスタンスというが、クラス以外でのインスタンスがあるのか不明。クラスからnewされたメモリ実体のことをインスタンスと呼ぶのだと思っていた。インスタンスと読んではまずいのだろうか？

http://postd.cc/pythons-objects-and-classes-a-visual-guide/

### ほかの言語との差異

* Module-3 にあるような、オブジェクトのメンバをメソッドから参照するための短縮した記法は使えません
    * メソッド関数の宣言では、オブジェクト自体を表す第一引数を明示しなければなりません
        * 第一引数のオブジェクトはメソッド呼び出しの際に暗黙の引数として渡されます
* Smalltalk に似て、クラスはそれ自体がオブジェクトです。そのため、 import や名前変更といった操作が可能です。
* C++ や Modula-3 と違って、ユーザーは組込み型を基底クラスにして拡張を行えます。
* C++ とは同じで Modula-3 とは違う点として、特別な構文を伴うほとんどの組み込み演算子 (算術演算子 (arithmetic operator) や添字表記) はクラスインスタンスで使うために再定義できます。

C++, Modula-3につづき、[Smalltalk](https://ja.wikipedia.org/wiki/Smalltalk)という言語まで出てきた。C++しか知らない。

### オブジェクト指向の意味論

> (クラスに関して普遍的な用語定義がないので、 Smalltalk と C++ の用語を場合に応じて使っていくことにします。 C++ よりも Modula-3 の方がオブジェクト指向の意味論が Python に近いので、 Modula-3 の用語を使いたいのですが、ほとんどの読者は Modula-3 についてしらないでしょうから。)

とても大事なことをさらっと言っている。[Modula-3](https://ja.wikipedia.org/wiki/Modula-3)の情報がほとんどないので困る。C++,Java,C#のようなメジャーなオブジェクト指向とは違うということか。本質的な部分の理解ができない。

