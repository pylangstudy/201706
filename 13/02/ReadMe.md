# [8.6. クリーンアップ動作を定義する](https://docs.python.jp/3/tutorial/errors.html#defining-clean-up-actions)

< [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## finally

> どんな状況でも必ず実行されます

絶対だな？試してやろうじゃないか。

### try-finally

```python
try:
    print('try')
finally:
    print('finally')
```
```sh
$ python 0.py 
try
finally
```

`try-else`と同じ。

### try-except-finally

```python
try:
    print('try')
    raise Exception
except Exception as e:
    print('except')
finally:
    print('finally')
```
```sh
$ python 1.py 
try
except
finally
```

例外発生後でも実行できるのが`finally`。終了処理ができる。

### try-else-finally

```python
try:
    print('try')
#    raise Exception
except Exception as e:
    print('except')
else:
    print('else')
finally:
    print('finally')
```
```sh
$ python 2.py 
try
else
finally
```

間にelseがあろうと実行される。

### いじわるテスト

### else内でエラー

tryが完了してelseへ。もう大丈夫と安心していると、else内で例外発生！
```python
try:
    print('try')
except Exception as e:
    print('except')
else:
    print('else')
    raise Exception('else内で例外発生！')
finally:
    print('finally')
```
```sh
 $ python 3.py 
try
else
finally
Traceback (most recent call last):
  File "3.py", line 8, in <module>
    raise Exception('else内で例外発生！')
Exception: else内で例外発生！
```

### except内でエラー

tryがエラーに。でもexceptしているから安心、と思いきや、except内で例外発生！
```python
try:
    print('try')
    raise Exception('try内で例外発生！')
except Exception as e:
    print('except')
    raise Exception('except内で例外発生！')
else:
    print('else')
finally:
    print('finally')
```
```sh
$ python 4.py 
try
except
finally
Traceback (most recent call last):
  File "4.py", line 3, in <module>
    raise Exception('try内で例外発生！')
Exception: try内で例外発生！

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "4.py", line 6, in <module>
    raise Exception('except内で例外発生！')
Exception: except内で例外発生！
```

### 変態テスト

### yield

```python
def func():
    for i in [0, 1, 2]:
        try:
            print('try    「yieldだ、別れよう」'.format(i))
            yield
        finally:
            print('finally「私を捨てるの？させないわ」')

for i in func():
    pass
print('The End.')
```
```sh
$ python 8.py 
try    「yieldだ、別れよう」
finally「私を捨てるの？させないわ」
try    「yieldだ、別れよう」
finally「私を捨てるの？させないわ」
try    「yieldだ、別れよう」
finally「私を捨てるの？させないわ」
The End.
```

毎回くりかえす。1回だけで済むかと思ったが。

### return

```python
def func():
    try:
        print('try     「returnで切り抜ける！」')
        return
    finally:
        print('finally 「逃がしはせんよ！」')

func()
print('The End.')
```
```sh
$ python 5.py 
try 「returnで切り抜ける！」
finally 「逃がしはせんよ！」
The End.
```

まさかのreturnキャッチ。

### continue

```python
def func():
    for i in [0, 1, 2]:
        try:
            print('try    「continueで変質者finallyから逃げるわ！({0}回目)」'.format(i))
            continue
        finally:
            print('finally「逃がないよtryちゃん （；´Д`）ﾊｧﾊｧ」')

func()
print('The End.')
```
```sh
$ python 6.py 
try    「continueで変質者finallyから逃げるわ！(0回目)」
finally「逃がないよtryちゃん （；´Д`）ﾊｧﾊｧ」
try    「continueで変質者finallyから逃げるわ！(1回目)」
finally「逃がないよtryちゃん （；´Д`）ﾊｧﾊｧ」
try    「continueで変質者finallyから逃げるわ！(2回目)」
finally「逃がないよtryちゃん （；´Д`）ﾊｧﾊｧ」
The End.
```

yieldと同じく毎回。

### break

```python
def func():
    for i in [0, 1, 2]:
        try:
            print('try    「breakでfinally子を回避！」'.format(i))
            break
        finally:
            print('finally「私から逃げられるとでも思ったの？」')

func()
print('The End.')
```
```sh
$ python 7.py 
try    「breakでfinally子を回避！」
finally「私から逃げられるとでも思ったの？」
The End.
```

何もbreakできていないように見えてしまう。breakの概念がbreakしそう。

## まとめ

> どんな状況でも必ず実行されます

偽りなし。終了処理に使える。

