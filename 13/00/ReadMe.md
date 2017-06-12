# [8.4. 例外を送出する](https://docs.python.jp/3/tutorial/errors.html#raising-exceptions)

< [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## raise

`raise`で例外を送出できる。ほかのプログラミング言語では`throw`に当たる。

```python
raise Exceptionを継承したクラス(任意引数1, 任意引数2, 任意引数3, ...)
```

```python
>>> raise Exception
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception
```
```python
>>> raise NameError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError
>>> raise ValueError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError
```

可変長引数を渡せるようだ。
```python
>>> raise ValueError('ABC')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: ABC
>>> raise ValueError(123)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 123
>>> raise ValueError(123, 456)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: (123, 456)
```

名前付き引数は渡せなかった。
```python
>>> raise ValueError(123, 456, abc=789)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ValueError does not take keyword arguments
```

## 再送出

`except`節で`raise`するとキャッチした例外をそのまま投げる。

```python
try:
    print('try')
    raise Exception('エラーです。')
except:
    print('except')
    raise
```

```sh
$ python 0.py 
try
except
Traceback (most recent call last):
  File "0.py", line 3, in <module>
    raise Exception('エラーです。')
Exception: エラーです。
```
