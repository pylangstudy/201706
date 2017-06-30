# [11.6. 弱参照](https://docs.python.jp/3/tutorial/stdlib2.html#weak-references)

< [11. 標準ライブラリミニツアー — その 2](https://docs.python.jp/3/tutorial/stdlib2.html#brief-tour-of-the-standard-library-part-ii) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [ガベージコレクション](https://docs.python.jp/3/glossary.html#term-garbage-collection)

> Python は自動的にメモリを管理します (ほとんどのオブジェクトは参照カウント方式で管理し、ガベージコレクション(garbage collection)で循環参照を除去します)。オブジェクトに対する最後の参照がなくなってしばらくするとメモリは解放されます。

> このようなアプローチはほとんどのアプリケーションでうまく動作しますが、中にはオブジェクトをどこか別の場所で利用している間だけ追跡しておきたい場合もあります。残念ながら、オブジェクトを追跡するだけでオブジェクトに対する恒久的な参照を作ることになってしまいます。

## [weakref](https://docs.python.jp/3/library/weakref.html#module-weakref)

> weakref モジュールでは、オブジェクトへの参照を作らずに追跡するためのツールを提供しています。弱参照オブジェクトが不要になると、弱参照 (weakref) テーブルから自動的に除去され、コールバック関数がトリガされます。弱参照を使う典型的な応用例には、作成コストの大きいオブジェクトのキャッシュがあります:

```python
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])
```
```sh
$ python3 0.py 
10
Traceback (most recent call last):
  File "0.py", line 14, in <module>
    print(d['primary'])
  File "/usr/lib/python3.4/weakref.py", line 125, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

## 参考

* http://qiita.com/pashango2/items/fb1e5e79589279c5a861
* https://ja.wikipedia.org/wiki/%E5%BC%B1%E3%81%84%E5%8F%82%E7%85%A7

