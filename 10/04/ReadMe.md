# [6.4.2. パッケージ内参照](https://docs.python.jp/3/tutorial/modules.html#intra-package-references)

[6.4. パッケージ](https://docs.python.jp/3/tutorial/modules.html#packages) < [6. モジュール (module)](https://docs.python.jp/3/tutorial/modules.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 相対参照

> パッケージが (前述の例の sound パッケージのように) サブパッケージの集まりに構造化されている場合、絶対 import を使って兄弟関係にあるパッケージを参照できます。

> また、明示的な相対importを from module import name の形式の import 文で利用できます。この明示的な相対 import では、先頭のドットで現在および親パッケージを指定します。

絶対パス、相対パスと同じ概念のようだ。それを絶対import、相対importと表現しているように見える。import自体は動詞なので違和感あるが。

## 記法

コード|説明
------|----
* `from . import {モジュール名}`|記述したコードファイルと同じディレクトリにある{モジュール名}をとりこむ
* `from .. import {モジュール名}`|記述したコードファイルの1つ上の階層にある{モジュール名}をとりこむ
* `from ..{パッケージ名} import {モジュール名}`|記述したコードファイルの1つ上の階層にあるパッケージ配下にある{モジュール名}をとりこむ

## 謎

> 相対 import は現在のモジュール名をベースにすることに注意してください。メインモジュールの名前は常に "__main__" なので、Python アプリケーションのメインモジュールとして利用されることを意図しているモジュールでは絶対 import を利用するべきです。

何を言っているのかわからない。

* 「相対 import は現在のモジュール名をベースにする」の意味がわからない
    * 名前でなく、相対importの起点になるのではないのか？
* 「メインモジュールの名前は常に "__main__" なので」
    * モジュール名はファイル名と同じではなかったのか？
* 「Python アプリケーションのメインモジュールとして利用されることを意図しているモジュール」とはどんなモジュールのことを言っているのか？
* 「絶対 import を利用するべきです」
    * 「メインモジュールの名前は常に "__main__" なので」
        * なぜモジュール名が`__main__`だと`import`を利用するべきなのかわからない

## 疑問

1. `import ..{モジュール名}`のように使えるか？
1. 2階層以上上の親は参照できるか？ `from ....{パッケージ名} import {モジュール名}`

結論から言えば、どちらもできなかった。

## 疑問1: `import ..{モジュール名}`のように使えるか？

結論: できなかった。

`import ..module11`と書くことで一つ上の階層にあるモジュールを取り込めるか確かめてみた。

```sh
$ python call.py 
Traceback (most recent call last):
  File "call.py", line 1, in <module>
    from package1.package11 import *
  File "/tmp/2/package1/package11/module111.py", line 1
    import ..module11
           ^
SyntaxError: invalid syntax
```

* 2/
    * call.py
    * package1/
        * package11/
            * __init__.py
            * module111.py
        * __init__.py
        * module11.py

2/call.py
```python
from package1.package11 import *
print(dir())
module111.some_method()
```

2/package1/__init__.py
```python
__all__ = ['package11']
```
2/package1/module11.py
```python
def some_method():
    print('module11.some_method()')
```
2/package1/package11/__init__.py
```python
__all__ = ['module111']
```
2/package1/package11/module111.py
```python
import ..module11
def some_method():
    print('module111.some_method()')
    module11.some_method()
```

```python
```
```python
```
```python
```

## 疑問2: 2階層以上上の親は参照できるか？ `from ....{パッケージ名} import {モジュール名}`

`from ..package11 import module112`で1階層分だけ親にいるパッケージ配下のモジュールを参照する。

* 0/
    * call.py
    * package1/
        * package11/
            * __init__.py
            * module111.py
            * module112.py
        * package12/
            * __init__.py
            * module121.py
            * module122.py

```sh
$ python call.py 
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'module122']
module122.some_method()
module112.some_method()
```
0/call.py
```python
from package1.package12 import *
print(dir())
module122.some_method()
```
0/package1/package11/__init__.py
```python
__all__ = ['module112']
```
0/package1/package11/module112.py
```python
def some_method():
    print('module112.some_method()')
```
```python
__all__ = ['module122']
```
0/package1/package12/module122.py
```python
from ..package11 import module112
def some_method():
    print('module122.some_method()')
    module112.some_method()
```

## まとめ

相対importは使わず、絶対importで指定したほうが良さそう。

* 相対importは1階層分親までしか参照できない。中途半端。これなら絶対importで指定したほうが良さそう。
* [謎](#謎)理論でも相対importは使わないほうが良いという

