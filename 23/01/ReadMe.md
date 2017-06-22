# [10.3. コマンドライン引数](https://docs.python.jp/3/tutorial/stdlib.html#command-line-arguments)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [sys](https://docs.python.jp/3/library/sys.html#module-sys)

> glob モジュールでは、ディレクトリのワイルドカード検索からファイルのリストを生成するための関数を提供しています:

```python
import sys
print(sys.argv)
```
```sh
$ python 0.py abc defg hi jkl
['0.py', 'abc', 'defg', 'hi', 'jkl']
```

> getopt モジュールは、 sys.argv を Unix の getopt() 関数の慣習に従って処理します。より強力で柔軟性のあるコマンドライン処理機能は、 argparse モジュールで提供されています。

* [getopt](https://docs.python.jp/3/library/getopt.html#module-getopt)
* [getopt()](https://docs.python.jp/3/library/getopt.html#getopt.getopt)
* [argparse](https://docs.python.jp/3/library/argparse.html#module-argparse)

