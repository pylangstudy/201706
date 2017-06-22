# [10.4. エラー出力のリダイレクトとプログラムの終了](https://docs.python.jp/3/tutorial/stdlib.html#error-output-redirection-and-program-termination)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

[sys](https://docs.python.jp/3/library/sys.html#module-sys)

## std

> sys モジュールには、 stdin, stdout, stderr を表す属性も存在します。 stderr は、警告やエラーメッセージを出力して、 stdout がリダイレクトされた場合でも読めるようにするために便利です:

> glob モジュールでは、ディレクトリのワイルドカード検索からファイルのリストを生成するための関数を提供しています:

```python
import sys
#print(sys.stdin.read())
#print(sys.stdout.read()) # io.UnsupportedOperation: not readable
#print(sys.stderr.read()) # io.UnsupportedOperation: not readable

#print(sys.stdin.write('stdin.write')) # io.UnsupportedOperation: not writable
print(sys.stdout.write('stdout.write')) # stdout.write12
print(sys.stderr.write('stderr.write')) # 12\nstderr.write
```
```sh
 $ python 0.py abc defg hi jkl
stdout.write12
12
stderr.write
```

`12`が何なのか謎。ゴミデータ？

## sys.exit()

> sys.exit() は、スクリプトを終了させるもっとも直接的な方法です。

```python
import sys
sys.exit()
print('after exit()')
```
```sh
$ python 1.py 
```
