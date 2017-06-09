# [6.2. 標準モジュール](https://docs.python.jp/3/tutorial/modules.html#standard-modules)

< [6. モジュール (module)](https://docs.python.jp/3/tutorial/modules.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 標準モジュールライブラリ

> Python は標準モジュールライブラリを同梱していて、別の Python ライブラリリファレンスというドキュメントで解説しています。

* 「モジュール」はPythonソースコードファイルのこと
* 「ライブラリ」はモジュールの集合のことだと思う

### OS機能を利用するモジュール

> 幾つかのモジュールは言語のコアにはアクセスしないものの、効率や、システムコールなどOSの機能を利用するために、インタープリター内部にビルトインされています。そういったモジュールセットはまたプラットフォームに依存した構成オプションです。

> 例えば、 [winreg](https://docs.python.jp/3/library/winreg.html#module-winreg) モジュールは Windows システムでのみ提供されています。 1つ注目に値するモジュールとして、 [sys](https://docs.python.jp/3/library/sys.html#module-sys) モジュールは、全ての Python インタープリターにビルトインされています。 

### 対話モードで表示する記号

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
```

* `sys.ps1`: 対話モードの一次プロンプトで表示する記号
* `sys.ps2`: 対話モードの二次プロンプトで表示する記号

二次プロンプトはwhileやif文などの内容で、インデントすべき箇所に表示される。

> これらの二つの変数は、インタプリタが対話モードにあるときだけ定義されています。

### モジュール検索パス

```python
>>> sys.path
['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-i386-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']
```

追加もできるが、[追加しないほうが安全](https://github.com/pylangstudy/201706/tree/master/09/03#%E5%90%8C%E5%90%8D%E3%81%AE%E5%84%AA%E5%85%88%E9%A0%86%E4%BD%8D)。
```python
>>> sys.path.append('/tmp')
>>> sys.path
['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-i386-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages', '/tmp']
```

