# [5.7. 条件についてもう少し](https://docs.python.jp/3/tutorial/datastructures.html#more-on-conditions)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 条件式を使う構文

* `if`
* `while`

## 比較演算子

表記|意味
----|----
`<`|より小さい
`>`|より大きい
`<=`|以下
`>=`|以上
`==`|等しい
`!=`|等しくない
`is`|同一のオブジェクトである
`is not`|同一のオブジェクトでない
`in`|右辺のiterable内に左辺が含まれている
`not in`|右辺のiterable内に左辺が含まれていない

[以前まとめたもの](https://github.com/pylangstudy/201705/blob/master/29/01/ReadMe.md#%E6%AF%94%E8%BC%83%E6%BC%94%E7%AE%97%E5%AD%90)に`in`が追加された。

* `in`, `is` は数値演算子よりも低い優先順位である

## 論理演算子（ビット演算子）

表記|意味
----|----
`and`|論理積。左辺と右辺がTrueならTrueを返す
`or`|論理和。左辺または右辺のうち少なくとも1つがTrueならTrueを返す
`not`|否定。真偽値を反転させる

### and

```python
>>> True and True
True
>>> True and False
False
>>> False and False
False
```

### or

```python
>>> True or True
True
>>> True or False
True
>>> False or False
False
```

### not

```python
>>> not True
False
>>> not False
True
```

### 優先順位

> A and not B or C と (A and (not B)) or C が等価になるように、ブール演算子の中で、 not の優先順位が最も高く、 or が最も低くなっています。

```python
>>> True and not True or True
True
```
```python
>>> (True and (not True)) or True
True
```

### 短絡演算子

> ブール演算子 and と or は、いわゆる 短絡 (short-circuit) 演算子です。

http://qiita.com/gyu-don/items/a0aed0f94b8b35c43290

* `True or False`のとき、最初のTrueですでに真であることが確定しているため以降のFalseは評価しない
    * もし`or`の左辺と右辺が関数で、複雑な計算をするとき、無駄を省ける
        * 真偽が決定したときは計算せずに済むから

#### `or`で評価終了するか確認

`or`のとき左側でTrueになった時点で評価を終了する。

```python
def Cond1():
    print('Cond1')
    return True
def Cond2():
    print('Cond2')
    return True
    
print('----- or -----')
if Cond1() or Cond2():
    print('Finished!!')
print('----- and -----')
if Cond1() and Cond2():
    print('Finished!!')
```
```sh
----- or -----
Cond1
Finished!!
----- and -----
Cond1
Cond2
Finished!!
```

#### `or`でもFalseであるかぎり評価継続する確認

```python
def CondTrue():
    print('CondTrue')
    return True
def CondFalse():
    print('CondFalse')
    return False
    
print('----- True or False -----')
if CondTrue() or CondFalse():
    print('Finished!!')
print('----- False or True -----')
if CondFalse() or CondTrue():
    print('Finished!!')
```
```sh
$ python3 1.py 
----- True or False -----
CondTrue
Finished!!
----- False or True -----
CondFalse
CondTrue
Finished!!
```

### 式内で代入できない

> Python では、C 言語と違って、式の内部で代入を行えない

`==`のつもりで`=`と書いてしまい代入結果の値を真偽値として扱ってしまうことによる条件式バグを回避する。

```python
v = 10
if v = 20:
    print('Finished!!')
```
```python
$ python3 2.py 
  File "2.py", line 2
    if v = 20:
         ^
SyntaxError: invalid syntax
```

C言語なら以下のように真と判定されてしまう。

1. `v = 20` で `v` に `20` を代入する
1. `if 20`の比較式により真と判定する（`0`以外の整数値は真となる）

http://ideone.com/lLrUKa

### 論理演算の結果が真偽値にならない

> 短絡演算子の戻り値をブール値ではなくて一般的な値として用いると、値は最後に評価された引数になります。

```python
v = 10 or 20 or 30
print(v)
v = 10 and 20 and 30
print(v)
```

もはや真偽値ですらない。論理演算子の戻り値ですらない。わかりにくい。

C言語なら論理演算子の戻り値は真偽値で返るのでわかりやすい。

http://ideone.com/vl6Ydd

#### 偽になる値

ドキュメントで明記されていないが、偽として扱われる値がある。

* `False`
* `0`
* `None`
* `''` (長さゼロの空文字列)

```python
v = 10 or 20 or 30
print(v)
v = 0 or 20 or 30
print(v)
v = None or 20 or 30
print(v)
v = '' or 'a' or 'b'
print(v)
v = False or True
print(v)
```
```sh
$ python3 4.py 
True
10
20
20
a
```

短絡演算子`or`で1つ目が無視され2つ目が出力されている。このことから、1つ目の値, `0`, `None`, `''`, `False`, は偽として扱われると判明する。

Noneが偽になるのは予想できる。NoneはC言語でいう`NULL`と考える。`NULL`はマクロで実体は`0`。`0`は真偽値で偽だから偽になるのだろう。

しかし、空文字まで偽になってしまうのが理解しづらい。文字列はメモリ実体である。文字列変数はそのメモリの参照(先頭アドレス)である。内容が空であるとしてメモリ確保されるだろうから参照は`NULL`(`0`)ではないはず。それともPython言語では空文字リテラルを代入したら内部でNULL参照の代入と同じになるのだろうか？

## 以下、蛇足

#### 空文字とNoneチェックが一発でできる

`if s:`だけで。

```python
def check(s):
    if s:
        print(s)
    else:
        print('文字列 s は None または 空文字 です。')
check('')
check(None)
check('abcdefg')
```
```sh
$ python3 5.py 
文字列 s は None または 空文字 です。
文字列 s は None または 空文字 です。
abcdefg
```

もし1つずつ式を書くなら、以下のようになる。
```python
if None is s or 0 == len(s):
    print('文字列 s は None または 空文字 です。')
```
```sh
$ python3 6.py 
文字列 s は None または 空文字 です。
文字列 s は None または 空文字 です。
abcdefg
```

#### 空白文字はチェックできない

空白文字のチェックには`str.strip()`で両端の空白文字を削除する関数を使う。

* `if '' == s.strip():`
* `if 0 == len(s.strip()):`

もし`s`が`None`であれば`strip()`関数は持っていない。

* `if None is not s and '' == s.strip():`

もし`s`が`str`型でなければ`strip()`関数は持っていない。

* `if None is not s and isinstance(s, str) and '' == s.strip():`

丁寧にやると面倒。

* Pythonは静的型付けができない分、if文のチェックが増えてしまう

という問題に気づく。

##### Pythonの「短く書ける」に疑問

https://docs.python.jp/3/tutorial/appetite.html

> Python では、とてもコンパクトで読みやすいプログラムを書けます。

> C 言語, C++ 言語や Java のプログラムよりもはるかに短くなります。

以前、[「短い＝読みやすい」ではない](https://github.com/pylangstudy/201705/blob/b22e8ab66fa02cc2415054c26c08ee96e93d7732/27/00/ReadMe.md#%E7%9F%AD%E3%81%84%E8%AA%AD%E3%81%BF%E3%82%84%E3%81%99%E3%81%84%E3%81%A7%E3%81%AF%E3%81%AA%E3%81%84)と考えていた。Pythonの自称「読みやすさ」は盲信できない。今回はさらに「短く書ける」ことにも疑問を持った。

###### 静的型付けできないせいでコードが長くなるかエラーになる

> 変数や引数の宣言が不要です。

書いてある通り、毎回変数の宣言をしないことがタイプ数の削減になっている。しかし「静的型付けできない」という側面には触れていない。

* Pythonは静的型付けができない分、`if`文のチェックが増えてしまう
    * もしくは、`try-except`文で例外をキャッチすることになる
        * もしくは、単体テストコードによって確認することになる
            * さもなくば実行時エラーを起こす可能性を孕んだコードになる

対象とする処理のコード自体は短く書けても、正確性に欠けたコードとなる。それを補うためにif文、try文、単体テストコードを書くなら、短く書けるどころか長く書くことになる。もしくは短いコードのまま実行時エラーの可能性を孕んだコードになるのではないか？

###### 欠点について書かれていないドキュメント

欠点について明記されていないまま、`短く書くことができる`という長所だけ明記されている。コードの字面だけをみていると簡単そうにみえるが、その分多くの暗黙ルールを知らねばならない。はたしてそれを「読みやすい」と言えるかどうか。知っている人にとっては読みやすい。しかし、「知らない人」「忘れた人」にとっては「読めない」。

以下のif文でNoneと空文字チェックをしている。それを読み取るには、Noneが偽、空文字`''`が偽になるという仕様を知らねば読めない。
```python
s = ''
if s:
    print('s is None or Empty!!')
```

###### どちらがいいか判断不能

静的型付けしたほうが楽なのか、しないほうが楽なのか。

短く書くことができても、短く書いてしまうことで生じる上記問題を無視していいか。それをどう判断すればいいのか。1文ごとに判断せねばならない。コードとして形に残らないところで、余計な労力を使うことにならないか。結局どちらのほうが「短く」「読みやすい」のか。それをどう判断すればいいのか。

##### 短く書ける

Pythonは「対象コード自体は」短く書ける。ただ、静的型付けされていないから実行時エラーが起こりうる。それを補うコードを考えると総合的に書く量は増えると思う。しかし補うコードは無視して、どれだけ短くなるか見てみる。

###### 空白文字だけかチェック

Python
```python
s = '   '
if s.strip():
```

C言語には文字列の先頭と末尾にある空白文字を削除する関数がない。自作せねばならない。面倒すぎて書きたくない。

Java
```java
string s = "   ";
if (null == s || String.IsEmpty(s)) {}
```

C#
```csharp
String s = "   ";
if String.IsNullOrEmpty(s) {}
```
http://ideone.com/qcKI8G

###### NULLまたは空文字チェック

Python
```python
s = ''
if s:
```

C言語
```c
char *s = "";
if (NULL == s || 0 == strlen(s)) { printf("Null or Empty!!\n"); }
```
http://ideone.com/LkT3Qe

Java
```java
String s = "";
if (null == s || s.isEmpty()) {}
```
http://ideone.com/Z9LmSz

C#
```csharp
string s = "";
if String.IsNullOrEmpty(s) {}
```
http://ideone.com/qcKI8G

Pythonの短さが際立つ。「空文字を偽として扱う」ことを知っていれば「短く」「読みやすい」コードと言える。知らねばコードの意味がわからず「読めない」。
