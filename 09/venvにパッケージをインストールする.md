# venvにパッケージをインストールする

< [Python学習環境を用意する](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md)

## venvとは

[venv](https://docs.python.jp/3/library/venv.html)はPython内蔵のパッケージ仮想環境構築ツール。

## 目的

パッケージ間の依存関係を解消する。

## 方法

パッケージのインストールディレクトリを個別に分ける。

## 準備

Pythonを起動する。

[pyenvを有効化する](https://github.com/pylangstudy/201705/blob/master/27/pyenv%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B.md)。
```sh
$ bash -l
```

[Pythonのバージョンを指定](https://github.com/pylangstudy/201705/blob/master/27/pyenv%E3%81%A7Python3.6.1%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B.md#pyenv%E3%81%A7%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E3%82%92%E6%8C%87%E5%AE%9A%E3%81%99%E3%82%8B)し、確認する。
```sh
$ pyenv global 3.6.1
$ pyenv version
3.6.1
$ python -V
Python 3.6.1
$ pip -V
pip 9.0.1
```

## 手順

### 1. インストール先のディレクトリを用意する

```sh
$ cd ~/
$ mkdir -p venv/webapi/
```

### 2. 仮想環境をつくる

```sh
$ python3 -m venv ~/venv/webapi/
```

指定したパス配下に以下のファイルやディレクトリが作成される。

* bin/
* include/
* lib/
* pip-selfcheck.json
* pyvenv.cfg

### 3. 仮想環境を有効化する

```sh
$ source ~/venv/webapi/bin/activate
(webapi) $ 
```

成功するとターミナルの先頭が`(仮想環境ディレクトリ名) $ `となる

### 4. 仮想環境にパッケージをインストールする

ここでは`requests`パッケージをインストールする。
```sh
(webapi) $ pip install requests
```

この仮想環境にインストールされたパッケージを一覧するには以下。
```sh
(webapi) $ pip list
```

### 5. パッケージを利用したコードを実行する

```sh
(webapi) $ python test.py
```

test.py
```sh
import requests
r = requests.get('https://www.github.com')
print(r.text)
```

パッケージをインストールした仮想環境を有効にすることで、パッケージを`import`できる。

## 今後

Python3.6.1と、仮想環境に入れたパッケージを使うとき、以下のコマンドを打つこと。ターミナルを起動するたびに。

```sh
$ bash -l
$ source ~/venv/仮想環境名/bin/activate
```
```sh
(仮想環境名) $ 
```

