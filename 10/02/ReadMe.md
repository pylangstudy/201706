# [6.4. パッケージ](https://docs.python.jp/3/tutorial/modules.html#packages)

< [6. モジュール (module)](https://docs.python.jp/3/tutorial/modules.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## パッケージ

> パッケージ (package) は、Python のモジュール名前空間を “ドット付きモジュール名” を使って構造化する手段です。

### 実体

* モジュールはPythonソースコードファイルである
* パッケージはPythonソースコードファイルを含んだディレクトリである

### 表記

> `A.B` は、 `A` というパッケージのサブモジュール `B` を表します。

以下に例を示す。

* 0/
    * call.py
    * package/
        * module.py

0/
```sh
$ python3 call.py 
some_method()
```
0/call.py
```python
import package.module
package.module.some_method()
```
0/package/module.py
```python
def some_method():
    print('some_method()')
```

## 効果

名前重複の回避ができる。

> モジュールを利用すると、別々のモジュールの著者が互いのグローバル変数名について心配しなくても済むようになるのと同じように、ドット付きモジュール名を利用すると、 NumPy や Python Imaging Library のように複数モジュールからなるパッケージの著者が、互いのモジュール名について心配しなくても済むようになります。

以下に例を示す。

* 1/
    * call.py
    * package1/
        * module.py
    * package2/
        * module.py

1/
```sh
$ python3 call.py 
pakage1.module.some_method()
pakage2.module.some_method()
```
1/call.py
```python
import package1.module
import package2.module
package1.module.some_method()
package2.module.some_method()
```
1/package1/module.py
```python
def some_method():
    print('pakage1.module.some_method()')
```
1/package2/module.py
```python
def some_method():
    print('pakage2.module.some_method()')
```

* モジュール名(ファイル名)、関数名、が同じでも、パッケージ名(ディレクトリ名)が違うから名前重複を回避できる

## `__init__.py`

> あるディレクトリを、パッケージが入ったディレクトリとしてPython に扱わせるには、ファイル __init__.py が必要です。

> このファイルを置かなければならないのは、 string のようなよくある名前のディレクトリにより、モジュール検索パスの後の方で見つかる正しいモジュールが意図せず隠蔽されてしまうのを防ぐためです。

意味がわからない。「`__init__.py`ファイルを配置せずに`string`ディレクトリを作ったら、`string`標準モジュールがimportできなくなる」ということか？試してみる。

### 標準stringパッケージ

```python
>>> import string
>>> dir(string)
['ChainMap', 'Formatter', 'Template', '_TemplateMetaclass', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
```

そもそも、`string`という標準モジュールが存在することすら知らなかった。`ascii_letters`のような名前が定義されているようだ。

### 自作stringパッケージ

* 2/
    * call.py
    * string/

call.py
```python
import string
print(dir(string))
```
Python3.4.3
```python
$ python3 call.py 
['ChainMap', 'Formatter', 'Template', '_TemplateMetaclass', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
```
Python3.6.1
```python
$ python call.py 
['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
```

`string/`ディレクトリを作成し、`import string`しても何も定義していないはずである。しかし実際には、標準モジュールで定義された名前が表示されている。

つまり、「標準モジュール名と同一のディレクトリ(パッケージ)名を作ってしまったときは、`__init__.py`ファイルを置かないと参照できない」ということか。

しかし、まだ確信が持てない。以下を試してみる。

* `string/some_module.py`など独自モジュールを参照したときはどうなるのか？
* stringディレクトリ(パッケージ)ではなくstring.pyファイル(モジュール)のときはどうなるのか？

### 独自stringパッケージから独自モジュール参照

* 3/
    * call.py
    * string/
        * some_module.py

call.py
```python
import string
print(dir(string))
string.some_method()
```
module.py
```python
def some_method():
    print('pakage1.module.some_method()')
```
```sh
$ python call.py 
['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
Traceback (most recent call last):
  File "call.py", line 3, in <module>
    string.module.some_method()
AttributeError: module 'string' has no attribute 'module'
```

エラーになった。`string`モジュールは`module`という名前の属性を持っていない。
```
AttributeError: module 'string' has no attribute 'module'
```

標準モジュールの`string`は`module`という名前の属性を持っていない。`dir()`の結果にてわかっている。よって今回`import string`で参照しているのは独自パッケージの`string`ではなく、標準モジュールの`string`であるとわかる。

### 独自stringモジュール参照

* 4/
    * call.py
    * string.py

call.py
```python
import string
print(dir(string))
string.some_method()
```
module.py
```python
def some_method():
    print('string.some_method()')
```
```sh
$ python call.py 
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'some_method']
string.some_method()
```

独自モジュールが参照できた。しかし、標準モジュールは参照できなくなってしまった。この構成で標準モジュール`string`を参照する術はあるのだろうか？ないのかもしれない。

### __init__.pyを独自パッケージに含める

[独自stringパッケージから独自モジュール参照](#独自stringパッケージから独自モジュール参照)パターンに`__init__.py`を追加した。

* 5/
    * call.py
    * string/
        * some_module.py
        * __init__.py

call.py
```python
import string
print(dir(string))
string.some_method()
```
module.py
```python
def some_method():
    print('pakage1.module.some_method()')
```
```sh
$ python call.py 
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
Traceback (most recent call last):
  File "call.py", line 3, in <module>
    string.module.some_method()
AttributeError: module 'string' has no attribute 'module'
```

成功すると思ったがエラー。`string`は`module`属性を持っていない。しかし、`dir()`の結果をみると、標準stringモジュールで定義されているはずの`ascii_letters`などが見当たらない。つまり、`import string`では、独自パッケージ`string`を参照しているということだろう。

### `import パッケージ.モジュール`とする

[__init__.pyを独自パッケージに含める](#__init__.pyを独自パッケージに含める)パターンで、`import string`を`import string.module`に変更した。

* 6/
    * call.py
    * string/
        * some_module.py
        * __init__.py

6/call.py
```python
import string.module
print(dir(string))
string.module.some_method()
```
6/string/some_module.py
```python
def some_method():
    print('string.module.some_method()')
```
6/string/__init__.py はファイル内容が空である。

```sh
$ python call.py 
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'module']
string.module.some_method()
```

* `__init__.py`を配置しても標準モジュール`string`と、独自パッケージ`string`の両方を参照できるわけではない
* もしかして、`__init__.py`がなくても`import string.module`とすれば参照できるのでは？

### __init__.pyなしで`import string.module`

* 7/
    * call.py
    * string/
        * some_module.py

```python
import string.module
print(dir(string))
string.module.some_method()
```
```sh
$ python call.py 
Traceback (most recent call last):
  File "call.py", line 1, in <module>
    import string.module
ModuleNotFoundError: No module named 'string.module'; 'string' is not a package
```

`__init__.py`がない`string`ディレクトリの場合、参照されるのは標準モジュールの`string`らしい。

### `from ... import ...`文を使っても片方のみ

* 8/
    * call.py
    * string/
        * some_module.py
        * __init__.py

[from ... import ...](https://docs.python.jp/3/tutorial/modules.html#more-on-modules)文なら`from`の直後に書いた名前はロードされず、import直後に書いた名前だけをロードする。fromに独自stringを入れたら、ロードされずに済むかも？と思って試してみた。結果はロードされた。`__init.__py`がある独自パッケージが優先されるらしい。そして標準モジュールの`string`は参照できない。両方参照できる抜け道はなさそう。

```python
from string.module import some_method
import string
some_method()
print(dir(string))
print(string.ascii_lowercase('ABC'))
```
```sh
$ python call.py 
string.module.some_method()
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'module']
Traceback (most recent call last):
  File "call.py", line 5, in <module>
    print(string.ascii_lowercase('ABC'))
AttributeError: module 'string' has no attribute 'ascii_lowercase'
```

## まとめ

標準モジュールと同一名の独自モジュールやパッケージを作った場合、標準か独自のどちらか一方しか参照できない。

* 標準モジュールと同一名のパッケージがある場合:
    * パッケージ内に`__init__.py`がある場合:
        * `import {同一名}`とすると独自パッケージ側が取り込まれる
    * パッケージ内に`__init__.py`がない場合:
        * `import {同一名}`とすると標準モジュール側が取り込まれる
* 標準モジュールと同一名のモジュールがある場合:
    * `import {同一名}`とすると独自パッケージ側が取り込まれる

## 懸念

### 両方を参照することはできない

標準モジュールと同一名のモジュールまたはパッケージを独自に作った場合、標準と独自の両方を参照することができない。どちらか一方しか参照できない。

という認識は本当に合っているか？わからない。

#### 名前重複なら使えるのは1つだけ: 独自ライブラリ、標準ライブラリ

一体何のために名前重複を回避すべくパッケージを作るのか。あくまで自分のディレクトリ配下のみでの重複回避としてしか役立たない。もし、標準モジュールと同一名の独自パッケージか独自モジュールを作りたくて、なおかつ標準モジュールも使いたい場合、それが実現できないということか。中途半端ではないか？

#### 名前重複なら使えるのは1つだけ: 独自ライブラリ、標準ライブラリ、サードパーティ製ライブラリ

サードパーティ製ライブラリも標準ライブラリと同様の扱いなのだろうか。色々インストールしているうちに「両方使いたいが、名前重複して片方しか使えない」事態にならないか。

#### __init__.pyはどちらとして名前を使うか決めるだけ

「`__init__.py`には名前重複回避して両方使うことはできない」という認識であっているか？あくまで名前重複時、標準モジュール名でなく独自パッケージ名側を`import`する目的で使うものということか。

#### 名前を決めるのが難しくなる

すべての標準、サードパーティ製モジュール名を把握した上で、それを避けた、適切な名前にせねばならない。

独自パッケージの場合、最上位は絶対に重複しないような名前にしたほうが良い。しかし、意味不明な文字列や、冗長になりかねない。

たとえば、以下のようになれば名前重複はしにくい。`system`と`thirdparty`だけ避ければいいから。しかし実際はそうではないし、冗長になる。独自モジュール名を独特の重複しづらいものにするのが最善。

作者|import
----|-------
標準モジュール|`system.{標準パッケージ名}.{標準モジュール名}`
サードパーティ製モジュール|`thirdparty.{サードパーティ製パッケージ名}.{サードパーティ製モジュール名}`
独自モジュール|`this.{独自パッケージ名}.{独自モジュール名}`

名前重複のリスクを増やしてでも、短く書けることを優先したのだろう。

