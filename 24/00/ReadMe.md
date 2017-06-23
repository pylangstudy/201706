# [10.7. インターネットへのアクセス](https://docs.python.jp/3/tutorial/stdlib.html#internet-access)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [urllib.request](https://docs.python.jp/3/library/urllib.request.html#module-urllib.request)

```python
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)
```
```sh
$ python 0.py
<BR>Jun. 23, 06:26:36 PM EDT		Eastern Time

```

## [smtplib](https://docs.python.jp/3/library/smtplib.html#module-smtplib)

```python
import smtplib
server = smtplib.SMTP('localhost')
addr_from = 'メアド1'
addr_to = 'メアド2'
server.sendmail(addr_from, addr_to,
"""To: {1}
From: {0}
...
Beware the Ides of March.
日本語も送れるかな？
""".format(addr_from, addr_to))
server.quit()
```
```sh
...
ConnectionRefusedError: [Errno 111] Connection refused
```

エラーで確かめられなかった。どうやってlocalhost でメールサーバを動かすのか不明。

> (2つ目の例は localhost でメールサーバーが動いている必要があることに注意してください。)

### Yahooサーバに送信

[2.py](https://github.com/pylangstudy/201706/blob/master/24/00/2.py)でyahoo.co.jpのメールサーバに送信してみた。

しかしタイトルと本文がつかず。

### 日本語の本文を送信

[3.py](https://github.com/pylangstudy/201706/blob/master/24/00/3.py)で日本語を送信。タイトルと本文が送れた。しかし送り主の別名が指定した通りにならない。受信メールはブラウザからYahooメールページで確認した。

