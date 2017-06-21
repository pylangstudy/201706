# [9.9. ジェネレータ (generator)](https://docs.python.jp/3/tutorial/classes.html#generators)

< [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

> ジェネレータ(generator)は、イテレータを作成するための簡潔で強力なツールです。

## yield

> ジェネレータは通常の関数のように書かれますが、何らかのデータを返すときには yield 文を使います。そのジェネレータに対して next() が呼び出されるたびに、ジェネレータは以前に中断した処理を再開します (ジェネレータは、全てのデータ値と最後にどの文が実行されたかを記憶しています)。

## 例

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for v in reverse([1,2,3]): print(v, end=' ')
```
```sh
$ python 0.py 
3 2 1
```

[前回](https://github.com/pylangstudy/201706/tree/master/22/00#%E7%8B%AC%E8%87%AA%E5%AE%9F%E8%A3%85)と同じ内容だが、簡単に書ける。独自クラスを作り、__iter()__, __next()__メソッドを実装する必要がない。関数ひとつで実現できる。

### __iter__,__next__の自動作成

> ジェネレータでできることは、前の節で解説したクラスを使ったイテレータでも実現できます。ジェネレータの定義がコンパクトになるのは __iter__() メソッドと __next__() メソッドが自動で作成されるからです。

yieldで実装したほうが良さそう。__next__などの独自実装をしたほうがいい場面はあるのか？

### ローカル変数の自動保存

> ジェネレータのもう一つの重要な機能は、呼び出しごとにローカル変数と実行状態が自動的に保存されるということです。これにより、 self.index や self.data といったインスタンス変数を使ったアプローチよりも簡単に関数を書くことができるようになります。

インスタンス変数を用意せずに済む。1メソッドあたりに必要な変数だけに制限できるからコードも見やすい。

### StopIterationの自動送出

> 終了時に自動的に StopIteration を送出します。これらの機能を組み合わせると、通常の関数を書くのと同じ労力で、簡単にイテレータを生成できます。

いちいち条件式と`raise StopIteration`を書かずに済む。

