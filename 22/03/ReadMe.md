# [10.1. OSへのインタフェース](https://docs.python.jp/3/tutorial/stdlib.html#operating-system-interface)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [os](https://docs.python.jp/3/library/os.html#module-os)

> os モジュールは、オペレーティングシステムと対話するための多くの関数を提供しています

```python
import os
print(os.getcwd()) # Get Current Working Directory
print(os.system('mkdir some')) # シェルコマンド 戻り値: 0(正常終了), 256(mkdir: ディレクトリ `some' を作成できません: ファイルが存在します)
print(os.chdir('/tmp/some'))  # Change Current Working Directory 戻り値: None
print(os.getcwd())
```

someディレクトリがない場合。
```
$ python 0.py 
/tmp
0
None
/tmp/some
```

someディレクトリがある場合。
```
$ python 0.py 
/tmp
mkdir: ディレクトリ `some' を作成できません: ファイルが存在します
256
None
/tmp/some
```

### 名前重複の罠

> from os import * ではなく、 import os 形式を使うようにしてください。そうすることで、動作が大きく異なる組み込み関数 open() が os.open() で遮蔽されるのを避けられます。

これはひどい。open()関数の定義があるモジュールをimportしてしまうと、組み込み関数のopen()が上書きされてしまう。標準ライブラリ同士でさえこの有り様。Pythonの名前重複は破壊的。

## [dir()](https://docs.python.jp/3/library/functions.html#dir), [help()](https://docs.python.jp/3/library/functions.html#help)

> 組み込み関数 dir() および help() は、 os のような大規模なモジュールで作業をするときに、対話的な操作上の助けになります

```python
import os
print(dir(os))
print(help(os))
```

dir()は属性一覧、help()はヘルプ表示。英語なのでヘルプにならない助けて。

## [shutil](https://docs.python.jp/3/library/shutil.html#module-shutil)

> ファイルやディレクトリの日常的な管理作業のために、より簡単に使える高水準のインタフェースが shutil モジュールで提供されています:

[shutil](https://docs.python.jp/3/library/shutil.html#module-shutil)はshell utilityの略と思われる。リンク先をみても関数の名前がわかりづらい。Pythonは読み易くない。短く書くために短縮された名前が読みにくい。また、短縮されていないのも混在している。読みにくいだけでなく覚えづらくて書きづらい。

### 例

```python
import shutil
shutil.copyfile('2.txt', '2.copy.txt')
shutil.move('2.copy.txt', 'some')
```

以下のエラーが生じる。

#### ファイルがない

```sh
FileNotFoundError: [Errno 2] No such file or directory: '2.txt'
```

#### コピー先に既存である

```sh
shutil.Error: Destination path 'some/2.copy.txt' already exists
```

