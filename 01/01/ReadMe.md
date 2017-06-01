# [5.1.3. リストの内包表記](https://docs.python.jp/3/tutorial/datastructures.html#list-comprehensions)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## リスト内包表記

> リスト内包表記はリストを生成する簡潔な手段を提供しています。主な利用場面は、あるシーケンスや iterable (イテレート可能オブジェクト) のそれぞれの要素に対してある操作を行った結果を要素にしたリストを作ったり、ある条件を満たす要素だけからなる部分シーケンスを作成することです。

> スタックでは、最後に追加された要素が最初に取り出されます (“last-in, first-out”)。

### for

```python
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
print(x)
```
```sh
$ python3 0.py 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
9
```

> これはループが終了した後にも存在する x という名前の変数を作る (または上書きする) ことに注意してください。

xはfor文ブロック内だけのローカル変数だと思っていたが、外側のスコープからも参照できてしまうようだ。

### map()

```python
squares = list(map(lambda x: x**2, range(10)))
print(squares)
#print(x) # NameError: name 'x' is not defined
```
```sh
$ python3 0.py 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### 調べた

唐突に出てきた[map()](https://docs.python.jp/3/library/functions.html#map)関数。調べてみた。

> map(function, iterable, ...)

> function を、結果を返しながら iterable の全ての要素に適用するイテレータを返します。

#### 使ってみた

わかるようでわからない。自分でも書いてみる。

```python
yansu = list(map(lambda x: x + 'でやんす。', ['私は田中', '8時', '賽は投げられた', '銀の弾丸はない', '時は満ちた', '我思う。ゆえに我あり', '諦めたらそこで試合終了']))
print(yansu)
```
```
$ python3 2.py 
['私は田中でやんす。', '8時でやんす。', '賽は投げられたでやんす。', '銀の弾丸はないでやんす。', '時は満ちたでやんす。', '我思う。ゆえに我ありでやんす。', '諦めたらそこで試合終了でやんす。']
```

語尾で決め台詞を台無しにしてみた。

### `[式 for x in iterable]`

本題。リスト内包表記。先述の複数行forや、`map()`よりもスマートに書ける。

```python
squares = [x**2 for x in range(10)]
print(squares)
```
```sh
$ python3 3.py 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
squares = [x + 'は猫である' for x in ['我輩', '私', '拙者', '余', 'ミー']]
print(squares)
```
```sh
$ python3 4.py 
['我輩は猫である', '私は猫である', '拙者は猫である', '余は猫である', 'ミーは猫である']
```

#### リスト内包表記 forネスト

```python
squares = [x + 'は猫' + y + '。' for x in ['我輩', 'おいら', 'ミー'] for y in ['である', 'でやんす', 'ザマス']]
print(squares)
```
```sh
$ python3 5.py 
['我輩は猫である。', '我輩は猫でやんす。', '我輩は猫ザマス。', 'おいらは猫である。', 'おいらは猫でやんす。', 'おいらは猫ザマス。', 'ミーは猫である。', 'ミーは猫でやんす。', 'ミーは猫ザマス。']
```

#### リスト内包表記 forネスト＋if

```python
squares = [x + 'は猫' + y + '。' for i,x in enumerate(['我輩', 'おいら', 'ミー']) for j,y in enumerate(['である', 'でやんす', 'ザマス']) if i==j]
print(squares)
```
```sh
$ python3 6.py 
['我輩は猫である。', 'おいらは猫でやんす。', 'ミーは猫ザマス。']
```

`if`の条件に合致した要素のみ返す。

##### 今までの書き方

```python
squares = []
for i,x in enumerate(['我輩', 'おいら', 'ミー']):
    for j,y in enumerate(['である', 'でやんす', 'ザマス']):
        if i==j:
            squares.append(x + 'は猫' + y + '。')
print(squares)
```
```sh
$ python3 7.py 
['我輩は猫である。', 'おいらは猫でやんす。', 'ミーは猫ザマス。']
```

[4.8. 間奏曲: コーディングスタイル](https://docs.python.jp/3/tutorial/controlflow.html#intermezzo-coding-style)を守るなら今までの記法のほうが良いのでは？

> ソースコードの幅が 79 文字を越えないように行を折り返すこと。

### いくつか作ってみる

#### 2のn乗

```python
values = [2**i for i in range(10)]
print(values)
```
```sh
$ python3 8.py 
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

#### アホ

```python
answer = [str(i) + '(アホ)' for i in range(1,20) if ( (0 == (i % 3)) or (0 < str(i).find(str(3))) )]
print(answer)
```
```sh
$ python3 9.py 
['3(アホ)', '6(アホ)', '9(アホ)', '12(アホ)', '13(アホ)', '15(アホ)', '18(アホ)']
```

3と3のつく数字の時だけアホになるつもりが、アホになるときだけ狙い撃ちしていたアホ。

