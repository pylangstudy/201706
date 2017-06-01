# [5.1.1. リストをスタックとして使う](https://docs.python.jp/3/tutorial/datastructures.html#using-lists-as-stacks)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## スタック

> スタックでは、最後に追加された要素が最初に取り出されます (“last-in, first-out”)。

### `pop()`

```python
l = [1,2,3]
l.append(4)
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
```
```sh
$ python3 0.py 
[1, 2, 3, 4]
4
[1, 2, 3]
3
[1, 2]
2
[1]
1
[]
Traceback (most recent call last):
  File "0.py", line 12, in <module>
    print(l.pop())
IndexError: pop from empty list
```

* `pop()`で後ろから取り出す
* 1つもないときに取り出そうとすると`IndexError`になる

