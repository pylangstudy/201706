# [6.1.2. モジュール検索パス](https://docs.python.jp/3/tutorial/modules.html#the-module-search-path)

[6.1. モジュールについてもうすこし](https://docs.python.jp/3/tutorial/modules.html#more-on-modules) < [6. モジュール (module)](https://docs.python.jp/3/tutorial/modules.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## モジュールを探す場所と順序

> spam という名前のモジュールをインポートするとき、インタープリターはまずその名前のビルトインモジュールを探します。

> 見つからなかった場合は、 spam.py という名前のファイルを sys.path にあるディレクトリのリストから探します。

## `sys.path`

> * 入力されたスクリプトのあるディレクトリ (あるいはファイルが指定されなかったときはカレントディレクトリ)。

> * PYTHONPATH (ディレクトリ名のリスト。シェル変数の PATH と同じ構文)。

> * インストールごとのデフォルト。

### 調べてみた

0.py
```python
import sys
print(sys.path)
```

Python3.4.3
```python
$ python3 0.py 
['/tmp', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-i386-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']
```

pyenv Python3.6.1
```python
$ python 0.py 
['/tmp', '/home/{user}/.pyenv/versions/3.6.1/lib/python36.zip', '/home/{user}/.pyenv/versions/3.6.1/lib/python3.6', '/home/{user}/.pyenv/versions/3.6.1/lib/python3.6/lib-dynload', '/home/{user}/.pyenv/versions/3.6.1/lib/python3.6/site-packages']
```

## あるvenvをactivateしたとき

```sh
(webapi) $ python3 0.py 
['/tmp', '/home/{user}/.pyenv/versions/3.6.1/lib/python36.zip', '/home/{user}/.pyenv/versions/3.6.1/lib/python3.6', '/home/{user}/.pyenv/versions/3.6.1/lib/python3.6/lib-dynload', '/.../venv/webapi/lib/python3.6/site-packages']
```

## pyenvを有効化し、Python3.6.1で上記venvをactivateしたとき

```sh
(webapi) $ python 0.py 
['/tmp', '/home/{user}/.pyenv/versions/3.6.1/lib/python36.zip', '/home/{user}/.pyenv/versions/3.6.1/lib/python3.6', '/home/{user}/.pyenv/versions/3.6.1/lib/python3.6/lib-dynload', '/.../venv/webapi/lib/python3.6/site-packages']
```

## 注釈

> シンボリックリンクを含むディレクトリはモジュール検索パスに追加 されません。

## 同名の優先順位

> 初期化された後、 Python プログラムは sys.path を修正することができます。スクリプトファイルを含むディレクトリが検索パスの先頭、標準ライブラリパスよりも前に追加されます。なので、ライブラリのディレクトリにあるファイルよりも、そのディレクトリにある同じ名前のスクリプトが優先してインポートされます。これは、標準ライブラリを意図して置き換えているのでない限りは間違いのもとです。より詳しい情報は 標準モジュール を参照してください。

sys.pathは修正しないほうが良さそう。標準ライブラリの名前など多すぎて把握できないから。
