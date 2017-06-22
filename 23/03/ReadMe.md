# [10.5. 文字列のパターンマッチング](https://docs.python.jp/3/tutorial/stdlib.html#string-pattern-matching)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [re](https://docs.python.jp/3/library/re.html#module-re)

> re モジュールでは、より高度な文字列処理のための正規表現を提供しています。

```python
import re
print(re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', '私は2000-01-01に生まれて2099-12-31に死にました。'))
print(re.sub(r'd..', r'AAA', 'abc def ghi abcdcba'))
print('吾輩は猫である。'.replace('猫', '神'))
```
```sh
$ python 0.py 
['2000-01-01', '2099-12-31']
abc AAA ghi abcAAAa
吾輩は神である。
```

