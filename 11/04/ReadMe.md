# [7.2.2. json による構造化されたデータの保存](https://docs.python.jp/3/tutorial/inputoutput.html#saving-structured-data-with-json)

< [7.2. ファイルを読み書きする](https://docs.python.jp/3/tutorial/inputoutput.html#reading-and-writing-files) < [7. 入力と出力](https://docs.python.jp/3/tutorial/inputoutput.html#input-and-output) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 記録するならjsonファイルが良い

> たとえば文字列 '123' のような文字列を、数値 123 に変換しなくてはならない

> 手作業でのパースやシリアライズは困難

> [JSON (JavaScript Object Notation)](http://json.org/) を使うことができます。

> 標準モジュール [json](https://docs.python.jp/3/library/json.html#module-json)

## 型変換

コード|変換
------|----
`json.dumps({"key": "value"})`|Python辞書型→JSON文字列
`json.loads('{"key": "value"}')`|JSON文字列→Python辞書型

```python
import json
print(json.dumps({"key": "value"}))
print(json.loads('{"key": "value"}'))
```
```sh
$ python 0.py 
{"key": "value"}
{'key': 'value'}
```

## ファイル間

コード|変換
------|----
`json.dump(d, file_object)`|Python辞書型をJSON文字列にしてファイルオブジェクトに書き出す。
`json.load(file_object)`|ファイルオブジェクトからJSON文字列を読み取り、パースしてPython辞書型を返す

```python
import json
with open('1.json', mode='w', encoding='utf-8') as f:
    d = {"key": "value"}
    json.dump(d, f)
with open('1.json', mode='r', encoding='utf-8') as f:
    d = json.load(f)
    print(d)
```
```sh
$ python 1.py 
{'key': 'value'}
```

