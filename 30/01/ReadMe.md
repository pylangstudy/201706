# [11.7. リスト操作のためのツール](https://docs.python.jp/3/tutorial/stdlib2.html#tools-for-working-with-lists)

< [11. 標準ライブラリミニツアー — その 2](https://docs.python.jp/3/tutorial/stdlib2.html#brief-tour-of-the-standard-library-part-ii) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

> 多くのデータ構造は、組み込みリスト型を使った実装で事足ります。とはいえ、時には組み込みリストとは違うパフォーマンス上のトレードオフを持つような実装が必要になこともあります。

## [array](https://docs.python.jp/3/library/array.html#module-array)

> array (配列) モジュールでは、array() オブジェクトを提供しています。配列はリストに似ていますが、同じ形式のデータだけが保存でき、よりコンパクトに保存されます。

> 以下の例では、通常 1 要素あたり 16 バイトを必要とする Python 整数型のリストの 代りに、2 バイトの符号無しの 2 進数 (タイプコード "H") の配列を使っています:

```python
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])
```
```sh
$ python3 0.py 
26932
array('H', [10, 700])
```

`B`だとunsigned char。-1を与えるとオーバーフローエラーになる。型チェックされている。
```python
from array import array
ary = array('B', [0, 255, 127]) # B: unsigned char 0〜255(0x00〜0xFF) 
#ary = array('B', [0, 255, -1]) # OverflowError: unsigned byte integer is less than minimum
for a in ary: print(a)
print(sorted(ary))
```
```sh
 $ python3 1.py 
0
255
127
[0, 127, 255]
```

hとiは同じ2Byte整数。
```python
from array import array
ary = array('b', [-128, 127])
ary = array('B  ', [0, 255])
ary = array('h', [-32768, 32767])
ary = array('H', [0, 65535])
ary = array('i', [-2147483648, 2147483647])
ary = array('I', [0, 4294967295])
ary = array('l', [-2147483648, 2147483647])
ary = array('L', [0, 4294967295])
ary = array('q', [int(-(2**64)/2), int((2**64)/2)-1])
ary = array('Q', [0, (2**64)-1])
ary = array('f', [0.0])
ary = array('d', [0.0])
```
```sh
$ python3 2.py 
```
