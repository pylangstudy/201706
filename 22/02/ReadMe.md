# [9.10. ジェネレータ式](https://docs.python.jp/3/tutorial/classes.html#generator-expressions)

< [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## ジェネレータ式

> 単純なジェネレータなら、式を使って簡潔にコードする方法があります。リスト内包に似た構文の式ですが、角括弧ではなく丸括弧を使います。ジェネレータ式は、関数の中でジェネレータをすぐに使いたいような状況のために用意されています。ジェネレータ式はコンパクトですが、完全なジェネレータに比べてちょっと融通の効かないところがありますが、同じ内容を返すリスト内包よりはメモリに優しいことが多いという利点があります。

### 例

```
sum(i*i for i in range(10))
```

### 書式

ジェネレータ式の構文は以下である。

```python
(式 for 変数 in iterable変数)
```

類似の構文についてまとめる。

構文|表記
----|----
リスト内包表記|`[式 for 変数 in iterable変数]`
辞書内包表記|`{式 for 変数 in iterable変数}`
ジェネレータ式|`(式 for 変数 in iterable変数)`

### sum()

Python文書の補足をする。[sum()](https://docs.python.jp/3/library/functions.html#sum)は組み込み関数である。反復可能(iterable)な要素の和(合計値)を返す。yieldは__iter__(),__next__()の自動実装をするイテラブル

### range()

[range()](https://docs.python.jp/3/library/functions.html#func-range)は組み込み関数である。指定した範囲内の値を反復可能(iterable)で返す。`
range(start, stop[, step])`の形式。startは開始値、stopは終了値、stepは刻み数。

## 例

ジェネレータ式。

```python
for v in (i+1 for i in [1,2,3]): print(v, end=' ')
```
```sh
$ python 0.py 
2 3 4
```

[前々回](https://github.com/pylangstudy/201706/tree/master/22/00#%E7%8B%AC%E8%87%AA%E5%AE%9F%E8%A3%85)、[前回](https://github.com/pylangstudy/201706/tree/master/22/01#%E4%BE%8B)と同様に逆順にする例。

```python
l = [1,2,3]
for v in (l[i] for i in range(len(l)-1, -1, -1)): print(v, end=' ')
```
```sh
$ python 1.py 
3 2 1
```

わずか2行で書けてしまった。

## まとめ

Pythonには繰り返し処理を短く書ける構文がある。高速化や省メモリなどパフォーマンスを制御したいときにもこの構文の使用を検討する必要がありそう。

構文|表記
----|----
リスト内包表記|`[式 for 変数 in iterable変数]`
辞書内包表記|`{式 for 変数 in iterable変数}`
ジェネレータ式|`(式 for 変数 in iterable変数)`

