# [9.5. 継承](https://docs.python.jp/3/tutorial/classes.html#inheritance)

< [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

> 言うまでもなく、継承の概念をサポートしない言語機能は “クラス” と呼ぶに値しません。

カプセル化の概念をサポートしない言語機能は“クラス”と呼ぶのか？

## 形式

> 派生クラス (derived class) を定義する構文は次のようになります:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

```python
class Human:
    def walk(self):
        print('walk.')
class Programmer(Human):
    def programming(self):
        print('programming.')

p = Programmer()
p.walk()
p.programming()
```
```sh
$ python3 0.py 
walk.
programming.
```

## ルール

* 基底クラス (base class) の名前 BaseClassName は、派生クラス定義の入っているスコープで定義されていなければなりません。
* 基底クラス名のかわりに任意の式を入れることもできます。
    * これは次の例のように、基底クラスが別モジュールで定義されているときに便利なことがあります:

らしいが、1件目と2件目が矛盾しているように見える。1件目の「されていなければなりません」と2件目の「こと"も"できます」が変。

### 同一スコープ内である必要はない

別モジュールは同一スコープなのか？モジュールごとに別スコープではないのか？

[9.2. Python のスコープと名前空間](https://docs.python.jp/3/tutorial/classes.html#python-scopes-and-namespaces)では以下の説明がある。

> スコープ (scope) とは、ある名前空間が直接アクセスできるような、 Python プログラムのテキスト上の領域です。“直接アクセス可能” とは、修飾なしに (訳注: spam.egg ではなく単に egg のように) 名前を参照した際に、その名前空間から名前を見つけようと試みることを意味します。

つまり、別モジュールによって定義されたら`module.Class`のように参照せねばならず、直接参照できない。これは「同一スコープ」とは言えないのでは？

それとも、`from package.module import class`のようにすれば、別モジュール定義を同一スコープ内に取り込めると言っているのか？しかし9.2章では「プログラムのテキスト上の領域」と言っている。別ファイルなら別領域であり同一ではないのでは？また、本9.5章では「クラス定義」と言っているが、それが「テキスト（Pythonソースコード）」を指しているのでは？

おそらく、どのファイルに書いていようが構わない。どんなimport方法であろうがOK。パッケージやモジュールなどフルネームでアクセスできればそれでいい。結果的に、[ルール](#ルール)の文章自体、要らないと思う。「同一ファイル内で定義したときの参照名と、外部ファイルに書いた時の参照名は違う」というだけの話。本章の本分である「継承」におけるルールではないと思う。

実際、以下の例が文書内で示されている。

```python
class DerivedClassName(modname.BaseClassName):
```

* https://github.com/pylangstudy/201706/tree/master/19/00/1/
* https://github.com/pylangstudy/201706/tree/master/19/00/2/

## 属性参照の解決

> 派生クラス定義の実行は、基底クラスの場合と同じように進められます。クラスオブジェクトが構築される時、基底クラスが記憶されます。記憶された基底クラスは、属性参照を解決するために使われます。要求された属性がクラスに見つからなかった場合、基底クラスに検索が進みます。この規則は、基底クラスが他の何らかのクラスから派生したものであった場合、再帰的に適用されます。

サブ(子,派生)クラスにない属性名の場合、スーパー(親,基底)クラスを探す。

* https://github.com/pylangstudy/201706/tree/master/19/00/3.py

## インスタンス生成

> 派生クラスのインスタンス化では、特別なことは何もありません。 DerivedClassName() はクラスの新たなインスタンスを生成します。

## メソッド参照の解決

> まず対応するクラス属性が検索されます。検索は、必要に応じ、基底クラス連鎖を下って行われ、検索の結果として何らかの関数オブジェクトがもたらされた場合、メソッド参照は有効なものとなります。

[属性参照の解決](#属性参照の解決)と同じことを言っているように読める。

## オーバーライド

> 派生クラスは基底クラスのメソッドを上書き (override) することができます。メソッドは同じオブジェクトの別のメソッドを呼び出す際に何ら特殊な権限を持ちません。このため、ある基底クラスのメソッドが、同じ基底クラスで定義されているもう一つのメソッド呼び出しを行っている場合、派生クラスで上書きされた何らかのメソッドが呼び出されることになるかもしれません。 (C++ プログラマへ: Python では、すべてのメソッドは事実上 virtual です。)

親クラスのメソッド名と同じ名前のメソッドを子クラスで作ったら上書きされる。その場合、子クラスのインスタンスからは上書きした子クラスのメソッドが呼び出される。親クラスのメソッドは呼び出せない。上書きされたからもう呼び出せない。ということか？

* https://github.com/pylangstudy/201706/tree/master/19/00/4.py

## 基底クラスのメソッドを呼び出す

> 派生クラスで上書きしているメソッドでは、基底クラスの同名のメソッドを置き換えるのではなく、拡張したいのかもしれません。基底クラスのメソッドを直接呼び出す簡単な方法があります。単に BaseClassName.methodname(self, arguments) を呼び出すだけです。この仕様は、場合によってはクライアントでも役に立ちます。 (この呼び出し方が動作するのは、基底クラスがグローバルスコープの BaseClassName という名前でアクセスできるときだけです。)

`super().method()`という別の呼び出し方もある。フルネームでクラス名を指定することも、第一引数にselfを渡すこともなく呼び出せる。

* https://github.com/pylangstudy/201706/tree/master/19/00/5.py

## `isinstance()`

> isinstance() を使うとインスタンスの型が調べられます。 isinstance(obj, int) は obj.__class__ が int や int の派生クラスの場合に限り True になります。

* https://github.com/pylangstudy/201706/tree/master/19/00/6.py

## `issubclass()`

> issubclass() を使うとクラスの継承関係が調べられます。 bool は int のサブクラスなので issubclass(bool, int) は True です。しかし、 float は int のサブクラスではないので issubclass(float, int) は False です。

* https://github.com/pylangstudy/201706/tree/master/19/00/7.py

