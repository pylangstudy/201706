# [10.12. バッテリー同梱](https://docs.python.jp/3/tutorial/stdlib.html#batteries-included)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 「バッテリー同梱」の哲学

> Python には “バッテリー同梱 (batteries included)” 哲学があります。この哲学は、洗練され、安定した機能を持つ Python の膨大なパッケージ群に如実に表れています。

https://ja.wikipedia.org/wiki/Python#.E3.83.A9.E3.82.A4.E3.83.96.E3.83.A9.E3.83.AA

> Pythonには「電池が付属しています（"Battery Included"）」の思想があり、プログラマがすぐに使えるようなライブラリや統合環境をあらかじめディストリビューションに含めるようにしている。このため標準ライブラリは非常に充実している。

バッテリー同梱の哲学とは、「すぐ簡単に使える」ということか？正直、サードパーティ製ライブラリ必須という印象なのだが…。

* pytz
* requests
* dataset
* pillow
* Beautiful Soup
* flask

.NET Frameworkのほうがはるかに充実していてしっかり作られている印象。Pythonの標準ライブラリは名付けなど雑に感じることが多い。しかし、標準ライブラリだけでも起動引数、iniファイル読取、HTTP通信など、やろうと思えばできることは確か。C言語の標準ライブラリよりはるかに充実している。

## [xmlrpc.client](https://docs.python.jp/3/library/xmlrpc.client.html#module-xmlrpc.client), [xmlrpc.server](https://docs.python.jp/3/library/xmlrpc.server.html#module-xmlrpc.server)

> 遠隔手続き呼び出し (remote procedure call) を全く大したことのない作業に変えてしまいます。モジュール名とは違い、XML を扱うための直接的な知識は必要ありません。

XML-RPCは通信規格の1つであるらしい。

### XML-RPC

* http://blanktar.jp/blog/2013/09/python-xml-rpc.html
* https://ja.wikipedia.org/wiki/XML-RPC

> XML-RPCとは、RPCプロトコルの一種

> エンコード（符号化）にXMLを採用し、転送機構にHTTPを採用している。非常に単純なプロトコルで、少数のデータ型やコマンドだけを定義しているだけであり、その仕様は2枚の紙にまとめられる。

> 新たな機能を追加したものがSOAP

> 類似の RPCプロトコルとして JSON-RPC がある

## [email](https://docs.python.jp/3/library/email.html#module-email)

> MIME やその他の RFC 2822 に基づくメッセージ文書を含む電子メールメッセージを管理するためのライブラリです。実際にメッセージを送信したり受信したりする [smtplib](https://docs.python.jp/3/library/smtplib.html#module-smtplib) や [poplib](https://docs.python.jp/3/library/poplib.html#module-poplib) と違って、email パッケージには (添付文書を含む) 複雑なメッセージ構造の構築やデコードを行ったり、インターネット標準のエンコードやヘッダプロトコルの実装を行ったりするための完全なツールセットを備えています。

以前、emailを以下のように使ってYahooメールサーバにメール送信した。

https://github.com/pylangstudy/201706/blob/master/24/00/3.py

## [json](https://docs.python.jp/3/library/json.html#module-json), [csv](https://docs.python.jp/3/library/csv.html#module-csv), [xml.etree.ElementTree](https://docs.python.jp/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree), [xml.dom](https://docs.python.jp/3/library/xml.dom.html#module-xml.dom), [xml.sax](https://docs.python.jp/3/library/xml.sax.html#module-xml.sax)

構造化テキストを解析するライブラリのことか。

> json パッケージはこの一般的なデータ交換形式のパースをロバストにサポートしています。

ロバストとは？

> コンピューターのプログラムが、起こったエラーに自動的に対処して処理を続行すること。 

https://kotobank.jp/word/%E3%83%AD%E3%83%90%E3%82%B9%E3%83%88-414553

## [sqlite3](https://docs.python.jp/3/library/sqlite3.html#module-sqlite3)

> SQLite データベースライブラリのラッパです

## [gettext](https://docs.python.jp/3/library/gettext.html#module-gettext), [locale](https://docs.python.jp/3/library/locale.html#module-locale), [codecs](https://docs.python.jp/3/library/codecs.html#module-codecs)

> 国際化に関する機能

タイトルのリンク先を見ても使い方がまったくわからない。以下のようなコードがあったが翻訳などされていない。コピペで動くコードを提供してくれないとわからない。

```python
import gettext
gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
gettext.textdomain('myapplication')
_ = gettext.gettext
# ...
print(_('This is a translatable string.'))
```
```sh
$ python3 0.py 
This is a translatable string.
```

ググってもよくわからない。

* http://akisute.blog.shinobi.jp/%E3%80%90%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%80%91/%E3%80%90python%E3%80%91gettext%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%82%92%E7%94%A8%E3%81%84%E3%81%A6%E5%9B%BD%E9%9A%9B%E7%9A%84%E3%81%AA%E7%94%B7%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F

以下でおおよその流れが掴めそう。しかし情報が古そう。python3.6.1との互換性はあるのか。

* http://d.hatena.ne.jp/fgshun/20100319/1269004530

### pygettext.py, msgfmt.py

* [pygettext.py](https://github.com/python/cpython/blob/master/Tools/i18n/pygettext.py)
* [msgfmt.py](https://github.com/hannosch/python-gettext/blob/master/pythongettext/msgfmt.py)

上記のツールが必要らしい。ググってコードファイルを入手。

### 翻訳用ファイル

国際化するためには以下3つの翻訳ファイルが必要らしい。その作成に上記2ツールを使う。

ファイル種別|作成コマンド|作成されるファイル
------------|-----------|------------------
pot|`python3 pygettext.py 0.py`|`messages.pot`
po|(messages.pot`をコピペして手動で翻訳編集)|`messages.po`
mo|`python3 msgfmt.py 0.py`|`messages.mo`

#### potファイル作成

```sh
$ python3 pygettext.py 0.py
```
```sh
$ ls
messages.pot
```

##### poファイル作成

`messages.pot`をコピペして`messages.po`とする。

`messages.po`を開くと以下のようになっている。
```pot
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2017-06-26 08:19+0900\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Generated-By: pygettext.py 1.5\n"


#: 0.py:6
msgid "This is a translatable string."
msgstr ""
```

以下の`msgstr ""`に翻訳した日本語を書く。
```pot
#: 0.py:6
msgid "This is a translatable string."
msgstr ""
```
```pot
#: 0.py:6
msgid "This is a translatable string."
msgstr "こいつは翻訳できる文字列だべや。"
```

ついでにヘッダも書き換える。

before
```
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR ORGANIZATION
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
```
after
```
# 0.py i18
# Copyright (C) 2017 ytyaru
# ytyaru <http://blog.hatena.ne.jp/ytyaru/ytyaru.hatenablog.com/>, 2017.
```

#### moファイル作成

```sh
$ python3 msgfmt.py messages.po
```
`messages.mo`ファイル作成されるはずだができない。

ここで詰まった。ググっても解決できず。情報が少なすぎる＆古すぎる＆動作しない。

## 所感

バッテリー同梱の哲学とは一体……

