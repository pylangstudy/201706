# [8.7. 定義済みクリーンアップ処理](https://docs.python.jp/3/tutorial/errors.html#predefined-clean-up-actions)

< [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## ファイルを閉じる

ファイルを開く場合、ファイルを閉じる操作とワンセットにすべき。さもないとファイルが開きっぱなしになって操作不能になる。と思う。

## withによるclose

```python
with open('some.txt', mode='w', encoding='utf-8') as f:
    f.write('ABC')
with open('some.txt', mode='r', encoding='utf-8') as f:
    print(f.read())
```
```sh
$ python3 0.py 
ABC
```

with文で書くと自動でファイルを閉じてくれる。べつの方法も以降に書くがwithが最善。

## ふつうにcloseを書く

```python
f = open('some.txt', mode='r', encoding='utf-8')
print(f.read())
f.close()
```
```sh
$ python3 1.py 
ABC
```

`f.close()`の間でエラーが起こったら実行されない。

## finallyでcloseする

```python
try:
    f = open('some.txt', mode='r', encoding='utf-8')
    print(f.read())
finally:
    f.close()
```
```sh
$ python3 2.py 
ABC
```

必ず`f.close()`が実行されるが冗長。

