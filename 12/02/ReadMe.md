# [8.3. 例外を処理する](https://docs.python.jp/3/tutorial/errors.html#handling-exceptions)

< [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 例外処理

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again")
```

標準入力で文字列を渡す。`int()`で数値化できたら終了する。できなければ`ValueError`例外が発生し、特定のエラーメッセージを表示してループをくりかえす。

```python
$ python 0.py 
Please enter a number: 123
```
```python
$ python 0.py 
Please enter a number: abc
Oops!  That was no valid number.  Try again
Please enter a number:
```

## KeyboardInterrupt例外の謎

KeyboardInterrupt例外のくだりの説明が意味不明だった。[まとめ](question_KeyboardInterrupt.md)。

## try文の動作

1. try内の文を実行する
1. try内の文でエラーが発生しなければexcept節をスキップする
1. try内の文でエラーが発生すると以降のtry文をスキップする
    1. 発生した例外がexcept節で指定された例外と一致するなら、そのexcept節の文を実行する
    1. 発生した例外がexcept節で指定された例外と一致しないなら、処理されない例外としてメッセージを出して実行を停止する

ということだと思う。しかし、この説明が意味不明だった。[まとめ](question_try.md)。

## except節

except節(ハンドラ)は以下のように書ける。

* 一つの try 文に複数の except 節を設けて、さまざまな例外に対するハンドラを指定することができる
* ハンドラは対応する例外だけを処理する（別の例外ハンドラで起きた例外は処理しない）
* except 節には複数の例外を丸括弧で囲ったタプルにして渡すことができる
* 最後の except 節では例外名を省いて既出以外のすべての例外をキャッチできる

```python
try:
    pass
except SyntaxError:
    pass
except ValueError:
    pass
```
```python
try:
    pass
except SyntaxError:
    pass
except (ValueError, NameError):
    pass
```
```python
try:
    pass
except SyntaxError:
    pass
except (ValueError, NameError):
    pass
except:
    raise
```

## Exceptionクラス継承と実行順

親クラスと子クラスのExceptionにおける実行順序を制御する方法。

```python
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
```sh
$ python 3.py 
B
C
D
```

> except 節が逆に並んでいた場合 (except B が最初にくる場合)、 B, B, B と出力されるはずだったことに注意してください — 最初に一致した except 節が駆動されるのです。

以下で確かめてみた。

```python
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")
```
```sh
$ python 4.py 
B
B
B
```

* C, DはBを継承した例外型である。よって、C, DはBとしてキャッチされる
* 子クラスの継承型を優先させたいときはexcept句を先に書く。親クラスのexcept句よりも先に。

## else節

> try ... except 文には、オプションで else 節 (else clause) を設けることができます。 

> 全ての except 節よりも後ろに置かなければなりません。

>  else 節は try 節で全く例外が送出されなかったときに実行される

ほかのプログラミング言語でいう`finally`とは別物のようだ。例外が発生すると実行されないから。

```python
try:
    print('try')
#    raise SyntaxError
#    raise ValueError
#    raise Exception
except SyntaxError:
    print('SyntaxError')
except (ValueError, NameError):
    print('ValueError, NameError')
except:
    print('except')
    raise
else:
    print('else')
```
```sh
$ python 5.py 
try
else
```
`raise SyntaxError`などで例外が発生したとき、`else`節は実行されない。

### 利用価値はあるのか？

無いと思う。[まとめ](question_else.md)

## 例外の引数

```python
try:
    raise Exception('引数1', '引数2')
except Exception as e:
    print(type(e))
    print(e)
    print(e.args)
```

## 呼出関数から発生したとしてもキャッチする

```python
def fails():
    x = 1 / 0

try:
    fails()
except Exception as e:
    print(type(e))
    print(e)
    print(e.args)
```
```sh
$ python 8.py 
<class 'ZeroDivisionError'>
division by zero
('division by zero',)
```

