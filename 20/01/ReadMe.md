# [9.6. プライベート変数](https://docs.python.jp/3/tutorial/classes.html#private-variables)

< [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

> オブジェクトの中からしかアクセス出来ない “プライベート” インスタンス変数は、 Python にはありません。

それがすべて。

## 慣習（人間による目視確認）

> しかし、ほとんどの Python コードが従っている慣習があります。アンダースコアで始まる名前 (例えば _spam) は、 (関数であれメソッドであれデータメンバであれ) 非 public なAPIとして扱います。これらは、予告なく変更されるかもしれない実装の詳細として扱われるべきです。

実際は`インスタンス._spam`とすればふつうに参照できてしまう。privateでも何でも無い。名前をつけるときに注意せねばならないことが増えるだけであり、何の役にも立たない。

## マングリング

> クラスのプライベートメンバについて適切なユースケース(特にサブクラスで定義された名前との衝突を避ける場合)があるので、マングリング(name mangling) と呼ばれる、限定されたサポート機構があります。 __spam (先頭に二個以上の下線文字、末尾に一個以下の下線文字) という形式の識別子は、 _classname__spam へとテキスト置換されるようになりました。ここで classname は、現在のクラス名から先頭の下線文字をはぎとった名前になります。このような難号化 (mangle) は、識別子の文法的な位置にかかわらず行われるので、クラス定義内に現れた識別子全てに対して実行されます。

書いてある通り、`インスタンス._classname__spam`とすると参照できてしまう。これがPythonにおける最も隠蔽できる方法である。

```python
class Human:
    def __init__(self):
        self.name = 'name'
        self._name = '_name'
        self.__name = '__name'

he = Human()
print(he.name)
print(he._name)
print(he._Human__name)
```
```sh
$ python3 0.py
name
_name
__name
```

### マングリングでは隠蔽できない

> 難号化の規則は主に不慮の事故を防ぐためのものだということに注意してください; 確信犯的な方法で、プライベートとされている変数にアクセスしたり変更することは依然として可能なのです。デバッガのような特殊な状況では、この仕様は便利ですらあります。

pythonではprivateにできない。カプセル化できない。重ねて言っているだけ。「デバッガなら便利」の意味がわからない。いつでも参照できることを便利と言っているのだろうか？警告したいのか、印象操作したいのか、ごちゃまぜ。どうしてもPythonはすばらしいという結論に導きたがっていることは良くわかった。

### オーバーライドに備えた親クラスメソッドの保持

> 名前のマングリングは、サブクラスが内部のメソッド呼び出しを壊さずにメソッドをオーバーライドするのに便利です。例えば:

```python
class Human:
    def __init__(self): self.__intro()
    def intro(self): print('Human')
    __intro = intro
    def show(self): self.__intro()
class Programmer(Human):
    def intro(self): print('Programmer')

p = Programmer()
p.intro()
p.show()
```
```sh
$ python3 1.py
Human
Programmer
Human
```

わざわざマングリングする必要があるのか？オーバーライドされてもHumanのselfはHumanではないのか？

#### selfとオーバーライド

```python
class Human:
    def __init__(self): self.intro()
    def intro(self): print('Human')
    def show(self): self.intro()
class Programmer(Human):
    def intro(self): print('Programmer')

p = Programmer()
p.intro()
p.show()
```
```sh
$ python3 2.py
Programmer
Programmer
Programmer
```

HumanのselfはProgrammerを参照するようだ。たしか`p.show()`は`Human.show(p)`と等価だった。つまり、第一引数selfはProgrammerのインスタンスになる。理解できた。

しかしそうなると、なぜProgrammerクラスのインスタンスで`_Human__intro()`メソッドが参照できるのか疑問である。`intro()`はオーバーライドされるからProgrammerクラスにも存在する。しかし、`__intro()`はHumanクラスだけが所有しているのでは？Programmerクラスからも参照できるのか？

#### instance._クラス__メソッド名

マングリングと同様の名前で参照できた。

```python
class Human:
    def __init__(self): self.__intro()
    def intro(self): print('Human')
    __intro = intro
class Programmer(Human):
    def intro(self):
        print('---------Programmer intro start----------')

#        super().__intro() # AttributeError: 'super' object has no attribute '_Programmer__intro'
        super()._Human__intro()
#        super()._Human__intro(self) # TypeError: intro() takes 1 positional argument but 2 were given

#        self.__intro() # AttributeError: 'Programmer' object has no attribute '_Programmer__intro'
        self._Human__intro() # プライベートメソッドも継承されているからselfで参照できる？
#        self._Human__intro(self) # TypeError: intro() takes 1 positional argument but 2 were given

        print('Programmer')
        print('---------Programmer intro end----------')

p = Programmer()
p.intro()
```
```sh
$ python3 3.py
Human
---------Programmer intro start----------
Human
Human
Programmer
---------Programmer intro end----------
```

子クラスから親クラスの`__メソッド名`メソッドを参照できる。`instance._クラス名__メソッド名`で。ただしinstanceには`self`または`super()`を用いる。

### 整理

* Pythonのオーバーライドはクラスによる継承の機能というより、名前重複による代入ではないか？
    * 親クラス定義内のselfが親クラスのインスタンスを指さず、子クラスを指してしまうため、オーバーライドされたメソッドを参照してしまうから
        * これを回避するために名前重複を避けるという
            * 名前重複回避のためにマングリング(`__メソッド名`による`instance._クラス名__メソッド名`化)を利用している
                * 結局、`_クラス名__メソッド名`という名前が重複したら、selfが指すオブジェクトのメソッドが呼び出されてしまう
                    * privateにできないから根本的な解決は不可能
                        * Pythonは全ての名前がpublicな仕様の言語である
                            * いつ、どこで、何を代入されるかわからない（代入されない保証ができない）
                                * Pythonは「定義」ができない

という解釈でいいのか？以下の疑問で検証してみる。

## 疑問

親の`_クラス名__メソッド名`関数オブジェクトに、子の関数オブジェクトを代入すれば、親メソッドが参照できなくなってしまうのでは？検証してみる。

```python
class Human:
    def __init__(self): self.__intro()
    def intro(self): print('Human')
    __intro = intro
    def show_human(self): self.__intro()
class Programmer(Human):
    def __init__(self):
        self._Human__intro = self.intro # p.show_human() とすると Human.__intro でなく Programmer.intro が実行される
    def intro(self):
        super().intro()
        print('Programmer')
        
p = Programmer()
p.intro()
p.show_human()
```
```sh
$ python3 6.py
<bound method Programmer.intro of <__main__.Programmer object at 0xb71325ac>>
<bound method Programmer.intro of <__main__.Programmer object at 0xb71325ac>>
Human
Programmer
Human
Programmer
```

`self._Human__intro = self.intro`をコメントアウトすれば、`p.show_human()`はHumanクラスのintroメソッドが実行される。

ようするに、たとえ`__変数名`を使ったとしても、意図して代入してしまえば上書きされてしまう。これはコンパイルエラーにならない。代入を禁止することもできない。いつ、どこで間違って代入されてしまうかわからない。Python言語はクラスを定義できない。動的に変更できてしまうのだから。この仕様のせいでバグを作りこんでしまうリスク増大。Python言語は大規模コードに向かないと思う。

## 結論

Pythonはすべてpublicである。privateにできない。変数名の先頭に`__`を付与するマングリングは名前を変化させるだけで実際はpublicな属性である。

つまりPythonはカプセル化できない。どこでもどのように変更されうるため、全コードを読まねば原因箇所を特定できない。大規模化するとメンテ不能に陥る可能性大。

ソフトウェアは複雑化、大規模化している。Pythonの貧弱な言語仕様では、後々バグ修正やテストなどのコストがかさむことが予想される。Pythonは小規模かつ単純な構造のときのみ利用するのが賢明か。

