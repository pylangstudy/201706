# try実行順の説明文が読み取れない

[8.3. 例外を処理する](https://docs.python.jp/3/tutorial/errors.html#handling-exceptions) < [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

> [try](https://docs.python.jp/3/reference/compound_stmts.html#try) 文は下記のように動作します。

のくだりの説明がよくわからなかった。

### 「try 文の後ろ」とはどこなのか？

> except 節が実行された後、 try 文の後ろへ実行が継続されます。

の意味がわからない。「try 文の後ろ」とはどこを指しているのか。try文以降に続くexcept節か？それともtry文内にある例外発生した文以降の文か？

もし前者なら、`except`節はすでに「try文の後ろ」だと思うので意味不明になる。「except 節が実行された後、 そのexcept節に実行が継続されます」となる。「try文で例外が発生した時点でtry文の実行を中断し、except節に実行が継続されます」なら理解できるのだが。

もし後者なら、ふつうのtry-catch構文ではありえない挙動となる。他のプログラミング言語なら、`try`→例外発生→対象例外キャッチ(`catch(except)`)→`finally`という流れのはず。一度例外をキャッチしたら、tryに戻ることはないはず。Pythonのtry文はそういう仕様なのか？以下のコードで確かめたが、戻ることはなかった。この解釈も違うらしい。

#### 例外発生後、tryに戻らないことを確認した

1. 以下のコードを実行する
1. わざと`a`など数値化できない文字列をわたして`ValueError`を発生させる
1. その後、try文に戻るなら、`print("try文完了！")`が表示されるはずである
1. try文に戻らないなら、`print("try文完了！")`は表示されないはずである
```python
while True:
    try:
        x = int(input("Please enter a number: "))
        print("try文完了！")
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again")
```
```sh
$ python 2.py 
Please enter a number: a
Oops!  That was no valid number.  Try again
Please enter a number: 
```
表示されなかった。例外キャッチしても、try文例外発生時点(`int(...)`)からの続き(`print("try文完了！")`)を実行されることはない。この挙動はほかのプログラミング言語と同様、ふつうのtry文の挙動だと思う。

`Please enter a number: `と再度表示されているのは、while文による繰り返しであり、try文の挙動ではない。本疑問は`try 文は下記のように動作します。`という前書きで説明されているとおり、try文の挙動についての説明なはずなので関係ないはず。また、「try 文の後ろ」を「エラー箇所の後ろ」とも解釈できないのでありえない。

## 謎まとめ

「try文の後ろ」とは一体どこのことを指しているのか？和訳がおかしいだけか？とりあえず他のプログラミング言語同様、「try文で例外が発生した時点でtry文の実行を中断し、except節に実行が継続されます」と解釈しておく。

