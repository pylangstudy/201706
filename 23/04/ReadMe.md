# [10.6. 数学](https://docs.python.jp/3/tutorial/stdlib.html#mathematics)

< [10. 標準ライブラリミニツアー](https://docs.python.jp/3/tutorial/classes.html#generator-expressions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [math](https://docs.python.jp/3/library/math.html#module-math)

> math モジュールは、浮動小数点演算のための C 言語ライブラリ関数にアクセスする手段を提供しています:

```python
import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))
```
```sh
$ python 0.py 
0.7071067811865476
10.0
```

## [random](https://docs.python.jp/3/library/random.html#module-random)

> random モジュールは、乱数に基づいた要素選択のためのツールを提供しています:

```python
import random
rnd = random.random()
print(rnd)
print(int(rnd * 100)) # 0..100
print(random.randrange(2)) # 0..1
print(random.choice(['大吉', '中吉', '小吉', '末吉', '凶', '大凶']))
```
```sh
$ python 1.py 
0.8800788532848068
88
0
中吉
```

## [statistics](https://docs.python.jp/3/library/statistics.html#module-statistics)

> statistics モジュールは数値データの基礎的な統計的特性（平均、中央値、分散等）を計算します:

```python
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data)) # 平均
print(statistics.median(data)) # 中央値
print(statistics.variance(data)) # 標本標準分散
```
```sh
$ python 2.py 
[2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
1.6071428571428572
1.25
1.3720238095238095
```

[SciPy プロジェクト](https://scipy.org) は数値処理のための多くのモジュールを提供しています。
