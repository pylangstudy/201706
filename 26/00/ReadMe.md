# [10.11. 品質管理](https://docs.python.jp/3/tutorial/stdlib.html#quality-control)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [doctest](https://docs.python.jp/3/library/doctest.html#module-doctest)

> doctest モジュールでは、モジュールを検索してプログラムの docstring に埋め込まれたテストの評価を行うためのツールを提供しています。

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```
```python
$ python3 0.py 
```
何もでない。成功なのだろうが、エラーがでるかどうか確認しないと動作しているかどうかもわからない。

### エラー確認

```python
def get_value():
    """Computes the arithmetic mean of a list of numbers.

    >>> print(get_value())
    [1,2,3]
    """
    return [1,2,3]

import doctest
doctest.testmod()   # automatically validate the embedded tests
```
```sh
$ python3 1.py 
**********************************************************************
File "1.py", line 4, in __main__.get_value
Failed example:
    print(get_value())
Expected:
    [1,2,3]
Got:
    [1, 2, 3]
**********************************************************************
1 items had failures:
   1 of   1 in __main__.get_value
***Test Failed*** 1 failures.
```

配列を対話モードでprintすると`[1, 2, 3]`のようにスペースが付与される。でも、docstringでは`[1,2,3]`と書いてしまっている。一致しないからエラー。

## [unittest](https://docs.python.jp/3/library/unittest.html#module-unittest)

> unittest モジュールは doctest モジュールほど気楽に使えるものではありませんが、より網羅的なテストセットを別のファイルで管理することができます:

```python
import unittest
def average(values): return sum(values) / len(values)

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

ポイントは以下。

* テスト用クラスを作る
    * unittest.TestCaseを継承する
        * テスト用メソッドの名前は先頭に`test`を付与する必要がある
            * `self.assert...`メソッドでテストケースを書く
* unittest.main()でテストを実行する

