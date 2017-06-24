# [10.8. 日付と時刻](https://docs.python.jp/3/tutorial/stdlib.html#dates-and-times)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [datetime](https://docs.python.jp/3/library/datetime.html#module-datetime)

> datetime モジュールは、日付や時刻を操作するためのクラスを、単純な方法と複雑な方法の両方で提供しています。日付や時刻に対する算術がサポートされている一方、実装では出力のフォーマットや操作のための効率的なデータメンバ抽出に重点を置いています。このモジュールでは、タイムゾーンに対応したオブジェクトもサポートしています。

不満な点がある。

* 月や日などは必ずゼロ埋めされてしまう
    * 10未満の場合、0埋めせずに表示する書式がない
        * `int(dt.strftime("%m")`のようなひと手間がいる
* １秒未満は`%f`で表示できるが、必ず6桁になる
    * 正確さの精度はせいぜい3桁までらしい
        * 3桁だけ表示する書式がない
* 曜日、月、和暦など日本固有カレンダーがない
* 週の始まりが月曜日。日曜日にしたいときどうすればいいのか
    * [calendar](https://docs.python.jp/3/library/calendar.html)の[setfirstweekday()](https://docs.python.jp/3/library/calendar.html#calendar.setfirstweekday)を使うらしい
    * `%W`で1年のうちの何週目かを取得できる
        * ゼロ埋めされている
        * 「週の始まりは月曜日としたとき、新年の最初の月曜日に先立つ日は 0週に属する」という面倒な計算(00..53)

```python
import datetime
now = datetime.date.today()
print(now)
datetime.date(2003, 12, 2)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = datetime.date(1964, 7, 31)
age = now - birthday
print(age)
print(age.days)
print(age.days/365)
```
```sh
$ python3 0.py 
2017-06-24
06-24-17. 24 Jun 2017 is a Saturday on the 24 day of June.
19321 days, 0:00:00
19321
52.93424657534246
```

