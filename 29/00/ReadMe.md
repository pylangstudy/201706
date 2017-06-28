# [11.4. マルチスレッディング](https://docs.python.jp/3/tutorial/stdlib2.html#multi-threading)

< [11. 標準ライブラリミニツアー — その 2](https://docs.python.jp/3/tutorial/stdlib2.html#brief-tour-of-the-standard-library-part-ii) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [threading](https://docs.python.jp/3/library/threading.html#module-threading)

0.txtファイルを適当に作って以下コードを実行。

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('0.txt', '0.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

```sh
$ python3 0.py 
The main program continues to run in foreground.
Finished background zip of: 0.txt
Main program waited until background was done.
```

ふつうに上から順で終わった。非同期かと思っていたのだが。

1.pyでAsyncZip.run()内にtime.sleep(2)を仕込んでみたが、`background.join()`で子スレッドが戻るまで停止するらしい（同期）。そこで、2.pyで`background.join()`で`background.join()`をコメントアウトすると、非同期になった。

```sh
$ python3 2.py 
The main program continues to run in foreground.
Main program waited until background was done.
Finished background zip of: 0.txt
```

完了通知や、成功・失敗したときのコールバック関数などは指定できないのだろうか？[threading](https://docs.python.jp/3/library/threading.html#module-threading)を流し読みしてもよくわからなかった。

まさかPythonには非同期スレッドの完了通知を受け取るしくみは無いのか？

