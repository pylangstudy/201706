# [8.1. 構文エラー](https://docs.python.jp/3/tutorial/errors.html#syntax-errors)

< [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## SyntaxError

`SyntaxError: invalid syntax`が構文エラー。

### コロンがない

以下の文でコロン`:`がないため`SyntaxError`になる。

```python
if True
    print('a')
```
```python
for a in [1,2,3]
    print(a)
```
```python
a = True
while a
    print('a')
    a = False
```
```python
def func()
    print('a')
```

コロン忘れは頻繁に起こる。これがかなりストレス。

* `{}`, `;`がなくても書けるのに`:`は必須。文脈と改行コードで解釈して欲しい
    * Pythonはインデントと`:`が必須なので、`{}`, `;`が必要なC言語とは違った面倒さがある

