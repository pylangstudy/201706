# [6.4.3. 複数ディレクトリ中のパッケージ](https://docs.python.jp/3/tutorial/modules.html#packages-in-multiple-directories)

[6.4. パッケージ](https://docs.python.jp/3/tutorial/modules.html#packages) < [6. モジュール (module)](https://docs.python.jp/3/tutorial/modules.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## `__path__`

> パッケージはもう一つ特別な属性として __path__ をサポートしています。

## コード

* 0/
    * call.py
    * package/
        * __init__.py
        * module.py

```sh
$ python call.py 
__path__: ['/tmp/0/package']
dir(): ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'package']
some_method()
```
call.py
```python
import package.module
print('dir():', dir())
package.module.some_method()
```
0/package/module.py
```python
def some_method():
    print('some_method()')
```
0/package/__init__.py
```python
__all__ = ['module']
print('__path__:', __path__)
```

## 使わないほうが良さそう

> この機能はほとんど必要にはならないのですが、パッケージ内存在するモジュール群を拡張するために使うことができます。

どこがどこを参照しているのか、わけがわからなくなりそう。使わないほうが良さそう。

