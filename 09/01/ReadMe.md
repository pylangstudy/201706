# [6.1. モジュールについてもうすこし](https://docs.python.jp/3/tutorial/modules.html#more-on-modules)

[6. モジュール (module)](https://docs.python.jp/3/tutorial/modules.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 実行文

> モジュールには、関数定義に加えて実行文を入れることができます。これらの実行文はモジュールを初期化するためのものです。これらの実行文は、インポート文の中で 最初に モジュール名が見つかったときにだけ実行されます。[1] (ファイルがスクリプトとして実行される場合も実行されます。)

```python
print('----- some_method_0 -----')
def some_method():
    print('some_method()')
```
```python
import some_module_0
some_module_0.some_method()
```
```sh
$ python3 call_0.py 
----- some_method_0 -----
some_method()
```

## モジュール内グローバル変数

```python
import some_module_1
global_var = 'call_1.py'
print(global_var)
print(some_module_1.global_var)
some_module_1.some_method()
```
```python
global_var = 'some_module_1.py'
print('----- some_method_0 -----')
def some_method():
    print('some_method()')
```
```sh
$ python3 call_1.py 
----- some_method_1 -----
call_1.py
some_module_1.py
some_method()
```

カプセル化できない恐ろしさ。

## import先でもimport可

> モジュールが他のモジュールを import することもできます。 

> import 文は全てモジュールの(さらに言えばスクリプトでも)先頭に置きますが、これは慣習であって必須ではありません。

call_2.py
```python
import some_module_2
some_module_2.some_method()
```
some_module_2.py
```python
def some_method():
    import some_module_2_0
    some_module_2_0.some_method()
```
some_module_2_0.py
```python
def some_method():
    print('some_module_2_0.py')
```
```sh
$ python3 call_2.py 
some_module_2_0.py
```

必須ではないからと言って、関数定義内で`import`することに弊害などはないのだろうか。

## `from ... import ...`

> import 文には、あるモジュール内の名前を、import を実行しているモジュールのシンボルテーブル内に直接取り込むという変型があります。

some_module_3.py
```python
def some_method():
    print('some_method')
```
call_3.py
```python
from some_module_3 import some_method
some_method()
#some_module_3.some_method() # NameError: name 'some_module_3' is not defined
```
```sh
$ python3 call_3.py 
some_method
```

> この操作は、import の対象となるモジュール名をローカルなシンボルテーブル内に取り入れることはありません

`some_module_3`モジュール名は参照できない。

## `from ... import *`

some_module_4.py
```python
from some_module_4 import *
some_method()
print(public)
#print(_private) # NameError: name '_private' is not defined
```
call_4.py
```python
public = 'public'
_private = 'private'
def some_method():
    print('some_method')
```
```sh
$ python3 call_4.py 
some_method
public
```

> アンダースコア (_) で始まるものを除いてすべての名前をインポートします。

> 殆どの場面で、Python プログラマーはこの書き方を使いません。未知の名前がインタープリターに読み込まれ、定義済みの名前を上書きしてしまう可能性があるからです。
> 一般的には、モジュールやパッケージから * を import するというやり方には賛同できません。というのは、この操作を行うとしばしば可読性に乏しいコードになるからです。しかし、対話セッションでキータイプの量を減らすために使うのは構わないでしょう。

`from ... import *`は使わないほうが良いらしい。

