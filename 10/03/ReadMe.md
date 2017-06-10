# [6.4.1. パッケージから * を import する](https://docs.python.jp/3/tutorial/modules.html#importing-from-a-package)

[6.4. パッケージ](https://docs.python.jp/3/tutorial/modules.html#packages) < [6. モジュール (module)](https://docs.python.jp/3/tutorial/modules.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## まとめ

https://docs.python.jp/3/tutorial/modules.html#packages

### `import`文

* `import {モジュール名}`
* `import {パッケージ名}.{モジュール名}`
* `import {パッケージ名}.{パッケージ名}...{モジュール名}`

呼び出すときはパッケージ名から始まるフルネームでなければならない。

```python
import package
package.module.some_method()
```

### `from ... import ...`文

* `from {モジュール名} import {関数名, 変数名}`
* `from {パッケージ名} import {モジュール名}`
* `from {パッケージ名}.{パッケージ名}... import {モジュール名}`

呼び出すときには`from`の直後にあるモジュール名やパッケージ名は不要。

```python
from package import module
module.some_method()
```

### `from ... import *`文

* `from {モジュール名} import *` [*](https://docs.python.jp/3/tutorial/modules.html#more-on-modules)
    * 関数名, 変数名をすべて取り込める
* `from {パッケージ名} import *`
    * {パッケージ名}配下にある別のパッケージを取り込みたいなら以下の対処が必要である
        * 対象パッケージ配下の`__init__.py`にて`__all__`変数に取り込みたいモジュール名を明記する
            * 例: `__all__ = ['sub_module1', 'sub_module2']`

#### ソースコード

`from {パッケージ名} import *`を使ってサブパッケージ配下のモジュールを取り込んでみる。

* 3/
    * call.py
    * package1/
        * __init__.py
        * package11/
            * __init__.py
            * module1.py
            * module2.py

```sh
$ python call.py 
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'module2']
module2.some_method()
```
3/package1/call.py
```python
from package1.package11 import *
print(dir())
module2.some_method()
```
3/package1/__init__.py
```python
__all__ = ['package11']
```
3/package1/package11/module1.py
```python
print('0/package/module1.py Run!!')
def some_method():
    print('module1.some_method()')
```
3/package1/package11/module2.py
```python
def some_method():
    print('module2.some_method()')
```
3/package1/package11/__init__.py
```python
__all__ = ['module2']
```

* `from ... import *`したときに取り込まれるパッケージやモジュールを指定する
    * `__init__.py`にて`__all__`に追加することで
* module1.pyには実行文がある
    * `from ... import *`したときに実行したくないので、`__all__`には含めていない
        * もしmodule1を取り込みたいなら`from package1.package11 import module1`のように個別に取り込むこと

## 以下、蛇足

今回は先述の`from {パッケージ名} import *`記法と`__all__`がわかればいい。以下はPython文書への愚痴である。

## `from {パッケージ名} import *`とすると？

先に結論を書いてしまったが、今回は`from {パッケージ名} import *`でサブパッケージ配下のモジュールを取り込む方法が本題。しかし文章をうまく読み取れず苦労したので、最初にまとめておいた。

## `from ... import *`文は使わないほうがいい

* ロード等に長い時間がかかってしまう
    * 不要なモジュールまでimportされる
        * そのモジュール内に実行文があれば実行されてしまう
            * 明示的にimportされたときだけ実行して欲しいなら、何らかの不都合が生じるかも知れない

というわけで「`from ... import *`文は使わないほうがいい」ということだけを覚えて終えても構わないと思う。

## わかりづらい表現

Python文書の表現がわかりにくくて読み取るのに苦労した。

> 理想的には、何らかの方法でファイルシステムが調べられ、そのパッケージにどんなサブモジュールがあるかを調べ上げ、全てを import する、という処理を望むことでしょう。

実際はどうなるか明記されないまま、以下の文に続く。

> これには長い時間がかかってしまうこともありますし、あるサブモジュールを import することで、そのモジュールが明示的に import されたときのみ発生して欲しい副作用が起きてしまうかもしれません。

つまり、「長い時間がかかる」「副作用がある」としても、「理想的には…」のくだりは実現できると読める。

[前章](https://docs.python.jp/3/tutorial/modules.html#more-on-modules)でも、とくに何もすることなく`from ... import *`を使えたことから、「何もする必要はない」と思える。

[前章](https://docs.python.jp/3/tutorial/modules.html#more-on-modules)

しかし、実際に`from パッケージ名 import *`記法でサブパッケージやその配下のモジュールを参照することはできなかった。`NameError`になった。[前章](https://docs.python.jp/3/tutorial/modules.html#more-on-modules)の場合はモジュール定義内が対象だからかもしれない。今回はサブパッケージ配下のモジュールを取り込みたい。その違いがあるのかも知れない。それについての説明も一切ない。

その説明をしないまま、以下の文に続く。

> 唯一の解決策は、パッケージの作者にパッケージの索引を明示的に提供させる というものです。

問題なのは「解決策」とあるが、一体何の「解決」について言っているのかが不明なことである。「長い時間がかかる」問題？「副作用がある」問題？答えは「`from パッケージ名 import *`記法でサブパッケージ配下のモジュールを参照できない」問題である。しかしその問題についてPython文書のどこにも書いていない。問題について書いていないのに、唐突に「解決」といわれても、何を解決しようとしているのかがわからない。これがPython文書の表現がわかりにくかった理由である。

### なぜわかりにく表現にしたのか邪推する

「Pythonはすばらしい言語です」と印象付けるためだと邪推する。

ここまでPython文書のチュートリアルを順に読んでいて感じたのだが、「Python言語では○○が<strong>できない</strong>」という表現をあからさまに避け、「Python言語では○○が<strong>できる</strong>」に言い換えていることが多いと感じた。

「できない」ことを伝えることを徹底的に排除し、「できる」ことばかりにフォーカスをあてて伝えている。これは印象操作に他ならない。よく知らないが、おそらく英語圏のプレゼンテーションのやり口なのだろう。

### Python初学者にふさわしくない表現方法である

Pythonコードの書き方を知りたいなら、端的にその記法や法則を示してくれればいい。できること、できないことをみせて理解しやすくして欲しい。実用書として。

しかしこの文書は「何ができないか」だけが隠されている。読み手がその裏を読み取ろうとせねばならない。初学者は右も左もわからないのだから「こうだ」といわれたら、それしか見えなくなる。他に情報をもっていないのだから。しかし、欠点を知らされないまま進めていくと、後で悩むこととなり時間を奪われる。

また、「できない」ことを隠すために周りくどい表現になっているせいで、読み取るのに苦労する。時間がかかるし、疲れる。一言「これはできない」と言ってくれたら一気に把握できることを、無理やり「できる」というポジティブな表現にするために周りくどい説明をしている。それに付き合わされている感に嫌気が差す。端的に概要を把握したいのに。

少なくともここまでのPython文書のチュートリアルは、何もわからない初学者を理解させるよう導くことよりも、好印象を植え付けることに注力していると感じた。じつは[チュートリアルのindex](https://docs.python.jp/3/tutorial/index.html)でそう言っている。

### 個人的に印象は最悪

できないことだけを隠されているように感じてしまう。それが騙してやろうとする悪意に感じる。実際、読み取るのことや、できないことは何かを試して探すのに時間がかかる。もちろん文書の存在自体、とてもありがたいものなのだが。

もし私なら[まとめ](#まとめ)で書いたように伝える。あれにファイル構成や最小限コードを書き足して、実行して確認できるようにする。初学者はまず最初に「どうすれば、何ができるか」を知りたいのだから。それによってどんな印象を持つかはその人次第でいい。

