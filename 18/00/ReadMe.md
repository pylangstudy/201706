# [9.3.5. クラスとインスタンス変数](https://docs.python.jp/3/tutorial/classes.html#class-and-instance-variables)

< [9.3. クラス初見](https://docs.python.jp/3/tutorial/classes.html#a-first-look-at-classes) < [9. クラス](https://docs.python.jp/3/tutorial/classes.html#classes) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

> 一般的に、インスタンス変数はそれぞれのインスタンスについて固有のデータのためのもので、クラス変数はそのクラスのすべてのインスタンスによって共有される属性やメソッドのためのものです:

## クラス変数

```python
class Human:
    last_name = 'ラストネーム'
    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        last_name = _last_name

taro = Human('太郎', '山田')
print('My name is {0} {1}'.format(taro.first_name, taro.last_name))
ichiro = Human('一郎', '鈴木')
print('My name is', ichiro.first_name, ichiro.last_name)
```
```sh
$ python3 0.py 
My name is 太郎 ラストネーム
My name is 一郎 ラストネーム
```

* クラス変数は全インスタンス共通である
* クラス変数はインスタンスからも参照できる
* クラス変数はインスタンスメソッドの`self`から参照できない
* クラス変数はインスタンスメソッドからnonlocal文, global文を使っても代入できない

## インスタンス変数

```python
class Human:
    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name
    def intro(self):
        print('My name is', self.first_name, self.last_name)

taro = Human('太郎', '山田')
ichiro = Human('一郎', '鈴木')
taro.intro()
ichiro.intro()
```

* インスタンス変数はインスタンス固有である
* インスタンス変数はインスタンスメソッドの`self`から参照できる

## クラス変数とインスタンス変数の使い分け

```python
class Human:
    count = 0
    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name
        Human.count += 1
    def intro(self):
        print('私の名前は', self.last_name, self.first_name, 'です。')
    def all_number():
        print('全人類数:', Human.count)

taro = Human('太郎', '山田')
ichiro = Human('一郎', '鈴木')
taro.intro()
ichiro.intro()
Human.all_number()
```
```sh
$ python3 2.py 
私の名前は 山田 太郎 です。
私の名前は 鈴木 一郎 です。
全人類数: 2
```

クラスは名前空間なので、クラス変数へのアクセスは名前空間を介して参照していることになる。パッと見、`Human.`と`self.`の違いがわかりにくい。どちらも自分自身ではないのか、と言いたくなる。`self`はインスタンスオブジェクト、`Human`はクラスオブジェクトである。

## クラスとインスタンスの違い

パッケージ、モジュール、クラスは名前空間の定義。インスタンスはメモリ寿命の操作。それがクラスとインスタンスの大きな違いだと思う。

