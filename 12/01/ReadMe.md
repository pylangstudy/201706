# [8.2. 例外](https://docs.python.jp/3/tutorial/errors.html#exceptions)

< [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## Pythonにおけるエラー

Pythonにおけるエラーは以下の2種類。

* 構文エラー (syntax error) 
* 例外 (exception) 

## 例外

> 実行中に検出されたエラーは 例外 (exception) と呼ばれ

### 例

[ゼロ除算エラー](https://docs.python.jp/3/library/exceptions.html#ZeroDivisionError)。ゼロで割ることはできない。
```python
>>> 10/0
ZeroDivisionError: division by zero
```
[名前エラー](https://docs.python.jp/3/library/exceptions.html#ZeroDivisionError)。その名前が未定義。
```python
>>> value
NameError: name 'value' is not defined
```
[型エラー](https://docs.python.jp/3/library/exceptions.html#TypeError)。その型では実行不可。
```python
>>> '1' + 1
TypeError: must be str, not int
```

### ほかの組み込み例外

> [組み込み例外](https://docs.python.jp/3/library/exceptions.html#bltin-exceptions) には、組み込み例外とその意味がリストされています。

