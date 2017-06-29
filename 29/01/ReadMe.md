# [11.5. ログ記録](https://docs.python.jp/3/tutorial/stdlib2.html#logging)

< [11. 標準ライブラリミニツアー — その 2](https://docs.python.jp/3/tutorial/stdlib2.html#brief-tour-of-the-standard-library-part-ii) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [logger](https://docs.python.jp/3/library/logging.html#module-logging)

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```
```sh
$ python 0.py 
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

> これは以下の出力を生成します:

正常に動作するコード例をください…。

以下で多機能であるようなことを匂わせているが、まともに動作するコードすら提示していないのだから信用できない。なぜ渋る？

> デフォルトでは、info() と debug() による出力は抑制され、出力は標準エラーに送信されます。選択可能な送信先には、email、データグラム、ソケット、HTTP サーバへの送信などがあります。新たにフィルタを作成すると、DEBUG、INFO、WARNING、ERROR、CRITICAL といったメッセージのプライオリティによって異なる送信先を選択することができます。

> ログ記録システムは Python から直接設定することもできますし、アプリケーションを変更しなくてもカスタマイズできるよう、ユーザが編集可能な設定ファイルによって設定することもできます。

### ファイル出力

探してみた。

* https://docs.python.jp/3/library/logging.html#module-logging
    * https://docs.python.jp/3/howto/logging.html#logging-basic-tutorial
        * https://docs.python.jp/3/howto/logging.html#logging-to-a-file
            * 「チュートリアル」といっているが「HowTo」だった。紛らわしい。今やっているチュートリアルにも動作するコードを書いて欲しかった…

```python
import logging
logging.basicConfig(filename='1.log',level=logging.DEBUG)
logging.debug('デバッグ')
logging.info('インフォ')
logging.warning('ワーニング')
```
1.log
```
DEBUG:root:デバッグ
INFO:root:インフォ
WARNING:root:ワーニング
```

* `1.log`ファイルを作成する
    * 既存なら追記される
* `DEBUG:root:`のように変な文字列が先頭に付く

