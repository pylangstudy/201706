# [7.1.1. 古い文字列書式設定方法](https://docs.python.jp/3/tutorial/inputoutput.html#old-string-formatting)

< [7.1. 出力を見やすくフォーマットする](https://docs.python.jp/3/tutorial/inputoutput.html#fancier-output-formatting) < [7. 入力と出力](https://docs.python.jp/3/tutorial/inputoutput.html#input-and-output) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## `sprintf()`

C言語の`sprintf()`フォーマット。

```python
>>> import math
>>> '%5.3f' % math.pi
'3.142'
>>> '%7.2f' % math.pi
'   3.14'
```

> より詳しい情報は [printf 形式の文字列書式化](https://docs.python.jp/3/library/stdtypes.html#old-string-formatting) にあります。

