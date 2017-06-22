# [10.2. ファイルのワイルドカード表記](https://docs.python.jp/3/tutorial/stdlib.html#file-wildcards)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [glob](https://docs.python.jp/3/library/glob.html#module-glob) によるファイル検索

> glob モジュールでは、ディレクトリのワイルドカード検索からファイルのリストを生成するための関数を提供しています:

```python
import glob
print(glob.glob('*.py'))
```
```sh
$ python 0.py 
['0.py']
```

前回は [shutil](https://docs.python.jp/3/library/shutil.html#module-shutil) モジュールにあると言っていたのに、今回は[glob](https://docs.python.jp/3/library/glob.html#module-glob) である。統一感がないし名前もわかりにくい。使いづらい。

> ファイルやディレクトリの日常的な管理作業のために、より簡単に使える高水準のインタフェースが shutil モジュールで提供されています

