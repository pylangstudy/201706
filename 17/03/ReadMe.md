# [9.3.3. インスタンスオブジェクト](https://docs.python.jp/3/tutorial/classes.html#instance-objects)

< [9.3. クラス初見](https://docs.python.jp/3/tutorial/classes.html#a-first-look-at-classes) < [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## インスタンスオブジェクトにできること

> ところで、インスタンスオブジェクトを使うと何ができるのでしょうか？インスタンスオブジェクトが理解できる唯一の操作は、属性の参照です。有効な属性の名前には二種類(データ属性およびメソッド)あります。

## 属性

> データ属性 (data attribute) は、これは Smalltalk の “インスタンス変数” や C++の “データメンバ” に相当します。データ属性を宣言する必要はありません。ローカルな変数と同様に、これらの属性は最初に代入された時点で湧き出てきます。

どうでもいいが、C++では「メンバ変数」という名前でよく知られていると思っていた。「湧き出てきます」という表現に笑った。

## クラス変数の削除？

> 例えば、上で生成した MyClass のインスタンス x に対して、次のコードを実行すると、値 16 を印字し、 x の痕跡は残りません:

「x の痕跡は残りません」の意味がわからない。`del クラス変数`とするとクラス変数の定義が削除されるという意味か？コードを書いて確かめた。

```python
class MyClass:
    counter = 0

x = MyClass()
while x.counter < 3: x.counter += 1
print(x.counter)
del x.counter
print(x.counter)
```
```sh
$ python3 0.py 
3
0
```

と思ったが、このコードは根本的に間違っていた。定義しているのはクラス変数だが、参照しているのはインスタンス変数である。

インスタンス変数は定義していないのに、なぜ参照できる？おそらく未定義の変数を最初に参照したら、自動生成してしまうのだろう。ローカル変数も宣言なしに代入式から書けてしまうし。

クラス変数とインスタンス変数についてまだPython文書には明確な情報が出ていない。が、違いがわからないと上記のようなコードを書いてしまいかねない。

### クラス変数の削除

```python
class MyClass:
    counter = 0

while MyClass.counter < 3: MyClass.counter += 1
print(MyClass.counter)
del MyClass.counter
print(MyClass.counter)
```
```sh
$ python3 1.py 
3
Traceback (most recent call last):
  File "1.py", line 7, in <module>
    print(MyClass.counter)
AttributeError: type object 'MyClass' has no attribute 'counter'
```

`del`する前は参照できた。しかし、`del`後は`AttributeError`。「`del クラス.クラス変数`とすると、クラスからクラス変数の定義(名前)が削除される」とわかる。

### インスタンス変数の削除

同様に、インスタンス変数でも確かめてみる。

```python
class MyClass:
    def __init__(self):
        self.counter = 0

x = MyClass()
while x.counter < 3: x.counter += 1
print(x.counter)
del x.counter
print(x.counter)
```
```sh
$ python3 2.py 
3
Traceback (most recent call last):
  File "2.py", line 9, in <module>
    print(x.counter)
AttributeError: 'MyClass' object has no attribute 'counter'
```

クラス変数のときと同様。「`del インスタンス.インスタンス変数`とすると、インスタンスからインスタンス変数の定義(名前)が削除される」とわかる。

## メソッド

> もうひとつのインスタンス属性は メソッド (method) です。メソッドとは、オブジェクトに “属している” 関数のことです。(Python では、メソッドという用語はクラスインスタンスだけのものではありません。オブジェクト型にもメソッドを持つことができます。例えば、リストオブジェクトには、 append, insert, remove, sort などといったメソッドがあります。とはいえ、以下では特に明記しない限り、クラスのインスタンスオブジェクトのメソッドだけを意味するものとして使うことにします。)

例によって解読が難しい。メソッドとは何か、の答えとして「インスタンス属性」「オブジェクトに属している関数」「クラスインスタンス」「クラスインスタンスだけのものではありません」という4つの表現をしている。

「クラスインスタンスだけのものではありません」については、それの名前すら判明していない。そんな概念があることすら知らない。そんな状態で「クラスインスタンスだけのものではありません」と言われても、何を言っているのか意味不明である。

また、「モジュール"オブジェクト"に属している関数」は「関数」と呼び「メソッド」とは呼ばないはず。だから「"クラス"オブジェクトに属している関数をメソッドと呼ぶ」というべきではないのか？

### オブジェクト、クラス、インスタンス？

そもそも、これまで「インスタンスとは何か」について書かれていなかった。ついでに、よくわかっていないが以下の謎用語について予想してみる。

* オブジェクト
* クラス
* インスタンス
* クラスオブジェクト
* クラスインスタンス
* インスタンスオブジェクト

用語|意味|コード
----|----|------|
オブジェクト|Python言語ではすべてが`Object`を継承したオブジェクトである。らしい。|(クラスオブジェクト、関数オブジェクト)
クラス|特定の型。|`class MyClass: ...`
インスタンス|クラスからメモリ上に実体化したもの。|`x = MyClass()`
クラスオブジェクト|クラス定義の実体。|`co = MyClass`
クラスインスタンス|インスタンスと同義のはず。メモリ実体の中でも「クラス」であることを強調しているが、クラス以外でインスタンスと呼ぶのか？|`x = MyClass()`
インスタンスオブジェクト|インスタンスと同義のはず。Python言語ではすべてがオブジェクトである。その中でも「インスタンス」であることを強調している|`x = MyClass()`

#### 呼び分けの必要性

クラス、インスタンスだけで十分では？

「○○オブジェクト」についても、「モジュールオブジェクト」「関数オブジェクト」「クラスオブジェクト」「strオブジェクト」など無数にある。「すべてがオブジェクトである」ならあえてつける必要はないのでは？モジュール、関数、クラス、str(文字列)、だけで通じると思うのだが、何か意味はあるのか？

おそらく文脈上、「オブジェクト」か「インスタンス」かを識別したいときに後ろにつけるのだろう。しかし「インスタンス」と言えば「クラスから生成されたもの」という意味になるはず。ならばあえて「インスタンスオブジェクト」などと表現する意味はあるのか？「インスタンス」と言えば済むのでは？

たとえば「モジュールインスタンスオブジェクト」という言葉は無いはず。モジュールはクラスではないためインスタンス生成できないはずだから。「モジュールオブジェクト」といえば伝わる。「モジュール」と言っても伝わるかもしれない。しかし、「Pythonコードファイル」を指しているのか、Pythonコード中でimportした参照名を言っているのかの区別がつかないかもしれない。参照名であるなら「モジュールオブジェクト」と言うべきで、ファイルなら「モジュール定義ファイル」とでも言えばいいのか。

しかし「関数オブジェクト」についてはファイルと呼び分ける必要があるのか？コードファイルに書かれた静的テキストと、Python言語でメモリ上に生成した関数オブジェクトを区別する必要はあるのか？コード側は「関数定義」とでも呼ぶのか？

用語が明確なら、その一覧が欲しい。もしかしたら、文脈毎に、それっぽい用語を使っているだけなのか？その判断すらつかない。

### クラスの属性にはメソッドと変数の2種類がある

> インスタンスオブジェクトで有効なメソッド名は、そのクラスによります。定義により、クラスの全ての関数オブジェクトである属性がインスタンスオブジェクトの妥当なメソッド名に決まります。

意味不明。無視して読み進める。

> 従って、例では、MyClass.f は関数なので、x.f はメソッドの参照として有効です。しかし、MyClass.i は関数ではないので、x.i はメソッドの参照として有効ではありません。

おそらく[9.3.2. クラスオブジェクト](https://docs.python.jp/3/tutorial/classes.html#class-objects)にあった以下のコードのことだろう。

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

どうやら「メソッドと変数は別物」と言いたかったらしい。

> x.f は MyClass.f と同じものではありません — 関数オブジェクトではなく、メソッドオブジェクト (method object) です。

結論から言ってもらいたかった。

## まとめ

* クラスからインスタンス生成して返されたものがインスタンスオブジェクトである
* インスタンスオブジェクトは属性の参照ができる
* 属性には2種類ある
    * 変数
    * メソッド
