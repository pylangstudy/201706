# [5.1.2. リストをキューとして使う](https://docs.python.jp/3/tutorial/datastructures.html#using-lists-as-queues)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## リスト内包表記

> リストをキュー (queue) として使うことも可能です。> この場合、最初に追加した要素を最初に取り出します (“first-in, first-out”)。

> しかし、リストでは効率的にこの目的を達成することが出来ません。
> キューの実装には、 collections.deque を使うと良いでしょう。

```python
from collections import deque
queue = deque([1,2,3])
queue.append(4)
print(queue)
queue.popleft()
print(queue)
```
```sh
$ python3 0.py 
deque([1, 2, 3, 4])
deque([2, 3, 4])
```

「リストをキューとして使う」というタイトルに裏切られた。キューを使うときは`list`でなく`collections.deque`を使うべし。

