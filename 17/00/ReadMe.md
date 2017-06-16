# [9.2.1. スコープと名前空間の例](https://docs.python.jp/3/tutorial/classes.html#scopes-and-namespaces-example)

< [9.2. Python のスコープと名前空間](https://docs.python.jp/3/tutorial/classes.html#python-scopes-and-namespaces) < [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

ついにコードが出た。

## コード

```python
def scope_test():
    def do_local():
        spam = "local"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal"

    def do_global():
        global spam
        spam = "global"

    spam = "test"
    do_local()
    print("In middle scope local:", spam)
    do_nonlocal()
    print("In middle scope nonlocal:", spam)
    do_global()
    print("In middle scope global:", spam)

scope_test()
print("In global scope:", spam)
```
```sh
$ python3 0.py 
In middle scope local: test
In middle scope nonlocal: nonlocal
In middle scope global: nonlocal
In global scope: global
```

> このとおり、(デフォルトの) ローカルな 代入は scope_test 上の spam への束縛を変更しませんでした。 nonlocal 代入は scope_test 上の spam への束縛を変更し、 global 代入はモジュールレベルの束縛を変更しました。

> またここから、 global 代入の前には spam に何も束縛されていなかったことも分かります。

相変わらずPython文書の日本語が怪しいが、[前回](https://github.com/pylangstudy/201706/tree/master/16/00)やった通り、[global](https://docs.python.jp/3/reference/simple_stmts.html#global)文と[nonlocal](https://docs.python.jp/3/reference/simple_stmts.html#nonlocal)文の機能がわかっていれば納得できる結果。

### グローバル(モジュール)変数`spam`はどこにある？

変数`spam`はグローバルスコープに存在しないように見える。`do_...()`の各ローカルスコープ、`scope_test()`のミドルスコープには存在している。しかし、モジュール直下には存在していないように見える。おそらく、グローバルスコープに存在しないときに`global 変数名`とされると、その時点でグローバル変数が作成されるのだろう。

念のため、以下のようにグローバルスコープ(モジュール直下)に`spam`変数を追加して変化を見てみた。

```python
spam = "global(module)"
def scope_test():
    def do_local():
        spam = "local"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal"

    def do_global():
        global spam
        spam = "global"

    spam = "test"
    do_local()
    print("In middle scope local:", spam)
    do_nonlocal()
    print("In middle scope nonlocal:", spam)
    do_global()
    print("In middle scope global:", spam)

print("In global scope before:", spam)
scope_test()
print("In global scope after:", spam)
```
```sh
$ python3 1.py 
In global scope before: global(module)
In middle scope local: test
In middle scope nonlocal: nonlocal
In middle scope global: nonlocal
In global scope after: global
```

これでバッチリ確認できた。

* スコープは、ローカル、グローバル、その中間(ミドル)の3種類ある
    * それぞれに`spam`という同一名の変数を用意する
* print文 `In middle scope ...` で参照しているのはミドルスコープの`spam`である
    * ローカルは`do_local()`関数終了時点で寿命が尽きるため参照されない
    * `nonlocal`文により`do_nonlocal()`関数内(ローカル)でもミドルスコープにある`spam`に代入できる
    * `global`文により`do_global()`関数内(ローカル)でもグローバルスコープにある`spam`に代入できる
        * ただしprint時に参照している`spam`がミドルスコープのものなら、表示されるのはミドルスコープの`spam`である
* print文 `In global scope ...` で参照しているのはグローバルスコープの`spam`である
    * `global spam`文で代入される前は、初期化時の`spam = "global(module)"`の値である
    * `global spam`文で代入された後は、その値になる

