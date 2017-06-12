# [8.5. ユーザー定義例外](https://docs.python.jp/3/tutorial/errors.html#user-defined-exceptions)

< [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)


## Exceptionクラス継承

> 新しい例外[クラス](https://docs.python.jp/3/tutorial/classes.html#tut-classes)を作成することで、独自の例外を指定することができます

> 例外は、典型的に Exception クラスから、直接または間接的に派生したものです。

0.py
```python
class MyBaseError(Exception):
    pass
class MySuperError(MyBaseError):
    pass

if __name__ == "__main__":
    raise MySuperError
```
```sh
$ python 0.py 
Traceback (most recent call last):
  File "0.py", line 7, in <module>
    raise MySuperError
__main__.MySuperError
```

## 概要

> 例外クラスでは、普通のクラスができることなら何でも定義することができますが、通常は単純なものにしておきます。大抵は、いくつかの属性だけを提供し、例外が発生したときにハンドラがエラーに関する情報を取り出せるようにする程度にとどめます。

```python
import datetime
class MyBaseError(Exception):
    pass
class MySuperError(MyBaseError):
    def __init__(self, message=None):
        self.__message = '{0:%Y-%m-%d %H:%M:%S} '.format(datetime.datetime.now()) + message
    @property
    def Message(self):
        return self.__message

if __name__ == "__main__":
    try:
        raise MySuperError('エラーメッセージですよ。')
    except MySuperError as e:
        print(e.Message)
```

メッセージに日時を追加するくらいなら許される？

## 

> 複数の別個の例外を送出するようなモジュールを作成する際には、そのモジュールで定義されている例外の基底クラスを作成するのが一般的なプラクティスです:

つまり、以下のようなお作法があるということか。

1. モジュールごとにそのモジュール用例外を作る
1. モジュールの細かいエラーは1を継承する

```python
import datetime
class Module2Error(Exception):
    def __init__(self, message=None):
        self.__message = '{0:%Y-%m-%d %H:%M:%S} [Module2] '.format(datetime.datetime.now()) + message
    @property
    def Message(self):
        return self.__message
class SuperError(Module2Error):
    def __init__(self, message=None):
        super().__init__("[超エラー] " + message )
class SmallError(Module2Error):
    def __init__(self, message=None):
        super().__init__("[小エラー] " + message )

if __name__ == "__main__":
    try:
        raise SuperError('なんかヒドイことになった。')
    except SuperError as e:
        print(e.Message)
```
```sh
$ python 2.py 
2017-06-13 08:13:04 [Module2] [超エラー] なんかヒドイことになった。
```

## 慣例

* 例外クラス名は`Error`で終わる
* モジュールごとに独自例外を定義する
    * モジュールごとに基底クラスを定義し、その派生を使う
* 例外クラスの実装内容はエラーに関する情報を取り出せる程度に留める

