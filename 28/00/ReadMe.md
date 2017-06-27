# [11.2. 文字列テンプレート](https://docs.python.jp/3/tutorial/stdlib2.html#templating)

< [11. 標準ライブラリミニツアー — その 2](https://docs.python.jp/3/tutorial/stdlib2.html#brief-tour-of-the-standard-library-part-ii) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [string](https://docs.python.jp/3/library/string.html#module-string).[Template](https://docs.python.jp/3/library/string.html#string.Template)

### [substitute()](https://docs.python.jp/3/library/string.html#string.Template.substitute)

* `...${placeholder}...`
* `...$placeholder ...`

```python
from string import Template
t = Template('私の名前は$nameです。職業は${job}です。$$10で雇えます。')
print(t.substitute(name='山田', job='サラリーマン'))
print(t.substitute(name='鈴木', job='F1レーサー'))
t = Template('My name is$name. job is ${job}. please $$10.')
print(t.substitute(name='Yamada', job='***'))
print(t.substitute(name='Suzuki', job='???'))
```
```sh
$ python3 0.py 
私の名前は山田です。職業はサラリーマンです。$10で雇えます。
私の名前は鈴木です。職業はF1レーサーです。$10で雇えます。
My name isYamada. job is ***. please $10.
My name isSuzuki. job is ???. please $10.
```

> テンプレートでは、$ と有効な Python 識別子名 (英数字とアンダースコア) からなるプレースホルダ名を使います。プレースホルダの周りを {} で囲えば、プレースホルダの後ろにスペースを挟まず、英数文字を続けることができます。

この文から`...$name ...`のように後ろにスペースが必要だと思っていた。しかし試してみた所、前後にスペースなしで問題なかった。`${}`を使うほうが視認性は高いか。

#### KeyError

> substitute() メソッドは、プレースホルダに相当する値が辞書やキーワード引数にない場合に KeyError を送出します。

```python
from string import Template
t = Template('私の名前は$nameです。職業は${job}です。$$10で雇えます。')
print(t.substitute(name='山田'))
```
```sh
$ python3 1.py 
Traceback (most recent call last):
  File "1.py", line 3, in <module>
    print(t.substitute(name='山田'))
  File "/usr/lib/python3.4/string.py", line 121, in substitute
    return self.pattern.sub(convert, self.template)
  File "/usr/lib/python3.4/string.py", line 111, in convert
    val = mapping[named]
KeyError: 'job'
```

### [safe_substitute()](https://docs.python.jp/3/library/string.html#string.Template.safe_substitute)

```python
from string import Template
t = Template('''名前: $name 職業: ${job} 所持: $item''')
print(t.safe_substitute(name='山田', job='勇者', item='薬草'))
print(t.safe_substitute(name='鈴木', job='戦士'))
print(t.safe_substitute(**{'name':'高橋', 'job':'魔女', 'item':'毒消し草'}))
monk = {'name':'吉本', 'job':'僧侶'}
print(t.safe_substitute(**monk))
```
```sh
$ python3 2.py 
名前: 山田 職業: 勇者 所持: 薬草
名前: 鈴木 職業: 戦士 所持: $item
名前: 高橋 職業: 魔女 所持: 毒消し草
名前: 吉本 職業: 僧侶 所持: $item
```

## Template継承クラス

プレースホルダの記号を任意のものに変更できる。

```python
import string
class BatchRename(string.Template):
    delimiter = '%'
```

例題のコードを動作するように変更した。
```python
import string
import time
import os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(string.Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
```

以下のようになる。

```sh
$ python3 3.py 
Enter rename style (%d-date %n-seqnum %f-format):  aaa_%d
img_1074.jpg --> aaa_28Jun17
img_1076.jpg --> aaa_28Jun17
img_1077.jpg --> aaa_28Jun17
```

しかし、%dの後ろにアンダーバーをつけるとエラーになった。

```sh
$ python3 3.py 
Enter rename style (%d-date %n-seqnum %f-format):  aaa_%d_
Traceback (most recent call last):
  File "3.py", line 13, in <module>
    newname = t.substitute(d=date, n=i, f=ext)
  File "/usr/lib/python3.4/string.py", line 121, in substitute
    return self.pattern.sub(convert, self.template)
  File "/usr/lib/python3.4/string.py", line 111, in convert
    val = mapping[named]
KeyError: 'd_'
```

そこで`%{d}`とすると成功した。
```sh
$ python3 3.py 
Enter rename style (%d-date %n-seqnum %f-format):  aaa_%{d}_
img_1074.jpg --> aaa_28Jun17_
img_1076.jpg --> aaa_28Jun17_
img_1077.jpg --> aaa_28Jun17_
```

### `_`はプレースホルダ名として認識される

`$placeholder`書式の場合、`$placeholder_`のようにすぐ後ろに`_`を付与すると`_`を含めたプレースホルダ名として認識されるらしい。以下、試してみた。

```python
from string import Template
t = Template('私の名前は$name_です。職業は${job}です。$$10で雇えます。')
print(t.substitute(name='山田'))
```
```sh
$ python3 4.py
KeyError: 'name_'
```

`$placeholder`より`${placeholder}`書式のほうが確実で視認性も良い。

