# [9.5.1. 多重継承](https://docs.python.jp/3/tutorial/classes.html#multiple-inheritance)

< [9.5. 継承](https://docs.python.jp/3/tutorial/classes.html#inheritance) < [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 形式

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

## 名前解決の順

継承順(左から右)。ただし左に親がいれば右より先。

> ほとんどのシンプルな多重継承において、

多重継承だけでも複雑なのに、シンプルでない多重継承まであるのか？

> 親クラスから継承される属性の検索は、深さ優先で、左から右に、そして継承の階層の中で同じクラスが複数出てくる（訳注: ダイアモンド継承と呼ばれます）場合に２度探索をしない、と考えることができます。なので、 DerivedClassName にある属性が存在しない場合、まず Base1 から検索され、そして（再帰的に） Base1 の基底クラスから検索され、それでも見つからなかった場合は Base2 から検索される、といった具合になります。

* 多重継承＝ダイアモンド継承？

0.py
```python
class Human:
    def __init__(self): self.type_name = 'Human'
class Elf:
    def __init__(self): self.type_name = 'Elf'
class HumanElf(Human, Elf):
    def __init__(self):
#        print(self.type_name) # AttributeError: 'HumanElf' object has no attribute 'type_name'
        super().__init__()
        print(self.type_name) # Human
        self.type_name = 'HumanElf'
        print(self.type_name) # HumanElf

he = HumanElf()
```
```sh
$ python3 0.py
Human
HumanElf
```

* 継承では最初に見つかったほうを参照するらしい
    * しかし、自分のクラスで同一名ができると自分のほうを参照する
* `super().変数名`では参照できない
    * `super().メソッド名`だけがサポートされているらしい

### super

> 実際には、それよりもう少しだけ複雑です。協調的な [super()](https://docs.python.jp/3/library/functions.html#super) の呼び出しのためにメソッドの解決順序は動的に変更されます。このアプローチは他の多重継承のある言語で call-next-method として知られており、単一継承しかない言語の super 呼び出しよりも強力です。

* `super()`が何者なのかよく知らない
    * これまで説明もなかった
        * リンク先に説明があるが、何を言っているのかさっぱりわからない
* 「協調的な [super()](https://docs.python.jp/3/library/functions.html#super) の呼び出し」とはどのようなことを言っているのか？
    * call-next-methodでググってもよく分からなかった

#### super()では変数を参照できない

1.py
```python
class Human:
    def __init__(self): self.type_name = 'Human'
class Elf:
    def __init__(self): self.type_name = 'Elf'
class HumanElf(Human, Elf):
    def __init__(self):
#        print(super().type_name) # AttributeError: 'super' object has no attribute 'type_name'
        super().__init__()
#        print(super().type_name) # AttributeError: 'super' object has no attribute 'type_name'

he = HumanElf()
```

publicな変数なのだから参照できて当然と思うはず。しかし、`super().親クラスのメンバ変数名`で参照できない。`self.親クラスのメンバ変数名`で行うしかない。もし子クラス側で同一名があれば親側は参照できなくなる。

言い換えてみる。親クラスのメンバ変数を参照するときは`self.変数名`で行う。にもかかわらず、親クラスのメンバメソッドを参照するときは`super().メソッド名`で行う。これがわかりにくい。

[super()](https://docs.python.jp/3/library/functions.html#super)のリンク先では「クラスの中でオーバーライドされた継承メソッドにアクセスするのに便利です。」と説明されている。しかし「メンバ変数にアクセスすることはできない」とは一言も説明されていない。またしてもこのPython文書特有の記法であるネガティブ表現をポジティブ表現で言い換えるやり口。

### 動的順序付け

> 多重継承の全ての場合に 1 つかそれ以上のダイヤモンド継承 (少なくとも 1 つの祖先クラスに対し最も下のクラスから到達する経路が複数ある状態) があるので、動的順序付けが必要です。例えば、全ての新形式のクラスは object を継承しているので、どの多重継承でも object へ到達するための道は複数存在します。基底クラスが複数回アクセスされないようにするために、動的アルゴリズムで検索順序を直列化し、各クラスで指定されている祖先クラスどうしの左から右への順序は崩さず、各祖先クラスを一度だけ呼び出し、かつ一様になる (つまり祖先クラスの順序に影響を与えずにサブクラス化できる) ようにします。まとめると、これらの特徴のおかげで信頼性と拡張性のある多重継承したクラスを設計することができるのです。さらに詳細を知りたければ、 https://www.python.org/download/releases/2.3/mro/ を見てください。

「動的順序付けが必要です。」というからプログラマがやる必要があると思ったのだが、最後に「これらの特徴のおかげで信頼性と拡張性のある多重継承したクラスを設計することができるのです。」とあるからPython言語が自動でやってくれているということか？ようするに「無駄なアクセスを最小化する」という話か？英語のページへ丸投げされたので無視。


