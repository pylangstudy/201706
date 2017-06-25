# [10.10. パフォーマンスの計測](https://docs.python.jp/3/tutorial/stdlib.html#performance-measurement)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## パフォーマンス

> Python ユーザの中には、同じ問題を異なったアプローチで解いた際の相対的なパフォーマンスについて知りたいという深い興味を持っている人がいます。Python は、そういった疑問に即座に答える計測ツールを提供しています。

> 例えば、引数の入れ替え操作に対して、伝統的なアプローチの代わりにタプルのパックやアンパックを使ってみたいと思うかもしれません。 timeit モジュールを使えば、パフォーマンスがほんの少し良いことがすぐに分かります:

時間計測のことらしい。メモリ消費量や計算量などは計測できないのか。

## [timeit](https://docs.python.jp/3/library/timeit.html#module-timeit)

```python
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
```

Python 2.7.6
```
$ python2.7 0.py 
0.0947160720825
0.0799539089203
```

Python 3.4.3
```python
$ python3.4 0.py 
0.10998404400015716
0.09526886200001172
```

Python 3.6.1
```python
$ python3.6 0.py 
0.13292185600039375
0.07734810299916717
```

Pythonのバージョンが上がる毎に遅くなっている。

### リスト内包表記の速度計測

```python
import timeit

def loop_range():
    return range(100, 1, 1)
def loop_for():
    a = []
    for i in range(100):
        a.append(i+1)
    return a
def loop_listin():
    return [i+1 for i in range(100)]

timeit.__dict__.update(loop_for=loop_for, loop_listin=loop_listin, loop_range=loop_range)
print(timeit.Timer('loop_range()').timeit(1))
print(timeit.Timer('loop_for()').timeit(1))
print(timeit.Timer('loop_listin()').timeit(1))
```
```sh
$ python 1.py 
1.026700010697823e-05
5.286999839881901e-05
2.8635000489884987e-05
```

forよりもリスト内包表記のほうが早い。でも、`range()`だけで済ませられるならもっと早い。
