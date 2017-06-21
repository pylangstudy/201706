# [9.7. 残りのはしばし](https://docs.python.jp/3/tutorial/classes.html#odds-and-ends)

< [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## クラスを構造体として使う

> Pascal の “レコード (record)” や、C 言語の “構造体 (struct)” のような、名前つきのデータ要素を一まとめにするデータ型があると便利なことがあります。空のクラス定義を使うとうまくできます:

```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```

dict型ではダメなのか？`isinstance()`で特定の型であることを確認したいときに便利なのかもしれない。

```python
john = {'name': 'Yamada', 'dept': 'computer lab', 'salary': 5}
print(john)
```
```sh
$ python3 0.py 
{'dept': 'computer lab', 'salary': 5, 'name': 'Yamada'}
```

## 異なるクラスでも同一名なら呼び出せる

> ある特定の抽象データ型を要求する Python コードの断片に、そのデータ型のメソッドをエミュレーションするクラスを代わりに渡すことができます。例えば、ファイルオブジェクトから何らかのデータを構築する関数がある場合、 read() と readline() を持つクラスを定義して、ファイルではなく文字列バッファからデータを取得するようにしておき、引数として渡すことができます。

意味不明。もう自然言語で書くのはやめてソースコードで表現して欲しい。

* 「抽象データ型」とは何か？
* 「ある特定の抽象データ型を要求する Python コードの断片」とはどんなものか？
* 「ある特定の抽象データ型のメソッド」とはデータ、型、メソッドのうちどれなのか？
* 「ある特定の抽象データ型のメソッドをエミュレーションする」とは何をすることか？
* 「ファイルオブジェクトから何らかのデータを構築する」のに「ファイルではなく文字列バッファからデータを取得する」とはどういうことか？

「もしかして同一名なら型が違っても呼び出せる」ことを言っているのか？コードで表現してみた。

```python
class Main:
    def run(self, reader):
        print(type(reader))
        for record in reader.read():
            print(record)
class TsvFileReader:
    def __init__(self, file_object):
        self.__f = file_object
    def read(self):
        result = []
        for line in self.__f: result.append(line[:-1].split('\t'))
        return result
class StringReader:
    def __init__(self, string): self.__s = string
    def read(self):
        result = []
        for line in self.__s.split('\n'): result.append(line.split('\t'))
        return result

m = Main()
s = StringReader("""name	age
Yamada	50
Tanaka	40
Wada	30""")
f = open('1.tsv')
t = TsvFileReader(f)

m.run(s)
m.run(t)
f.close()
```

同一名メソッドがあれば呼び出せる。これは継承でも抽象クラスでも何でも無い。制約できないから、たまたま偶然、名前が一致してしまい、間違って渡してしまっても動作する。もしくは、メソッド名を変更してもコンパイルエラーになってくれない。実行時にはじめてエラーを検出する。修正漏れが起こりうる。便利というより、危険と感じる。

## __self__

> インスタンスメソッドオブジェクトにも属性があります。 m.__self__ はメソッド m() の属しているインスタンスオブジェクトで、 m.__func__ はメソッドに対応する関数オブジェクトです。

またしても意味不明。頼むから動作確認できるコードを書いてくれ。

* インスタンスメソッドオブジェクトとは何か？
    * どうやって参照するのか？
    * 何の役に立つのか？（どんな場面で使うのか？）
* 「メソッドに対応する関数オブジェクト」というが、メソッドと関数はクラス内にあるか否かの違いだけで呼び方の違いではなかったのか？

意味を予想してコードを書いてみた。

```python
class MyClass:
    def method(self):
        print('method')

c = MyClass()
print(c.method) # インスタンスのメソッドオブジェクト
print(c.method.__self__) # インスタンスのクラスオブジェクト
print(c.method.__func__) # インスタンスメソッドオブジェクトの関数オブジェクト
```
```sh
$ python3 2.py 
<bound method MyClass.method of <__main__.MyClass object at 0xb70c7f4c>>
<__main__.MyClass object at 0xb70c7f4c>
<function MyClass.method at 0xb70b6bb4>
```

`<bound method ...`と`<function ...`のように記述が違う。メソッドオブジェクトと関数オブジェクトは別物らしい。もうわけがわからない。メソッドと関数の違いは何なのか。それがわからない原因は以下の内どれなのか。

* 自分の理解力がない
* 見落とした、忘れた
* 説明がおかしい
* 説明不足
* 翻訳のせいで意味不明

「深く考えず読み飛ばそう」という結論になる。これでは今まで適当にググって書いてきたときと同じ。理解が深まることなくあやふやなまま進めてしまい、後で大幅な修正を余儀なくされて無為な時間を過ごす。それを回避するためにきちんと学ぼうと公式文書を読んでいるのに、理解が深まらない。チュートリアルだから？
