# KeyboardInterrupt例外の謎

[8.3. 例外を処理する](https://docs.python.jp/3/tutorial/errors.html#handling-exceptions) < [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

KeyboardInterrupt例外のくだりの説明が意味不明だった

## KeyboardInterrupt例外が発生しない

> ユーザがプログラムに (Control-C か、またはオペレーティングシステムがサポートしている何らかのキーを使って) 割り込みをかけてプログラムを中断させることができるようにしています。

私の環境では、`Ctrl+C`キー押下しても無反応だった。Ctrl+Zで強制終了できるのだが、例外キャッチした様子もなく、Python実行そのものが終了してしまう。「オペレーティングシステムがサポートしている何らかのキーを使って」というのがポイントなのだろう。OSはLinuxMint17.3MATEなのだが、それに該当するキーが何なのか、存在するのかも不明。どうやったら調べられるのかも不明。Ctrl+Zで終了するのとは違うのか？

### どのキーで発生するのか不明

> ユーザが生成した割り込みは、 [KeyboardInterrupt](https://docs.python.jp/3/library/exceptions.html#KeyboardInterrupt) 例外が送出されることで通知されるということに注意してください。

[KeyboardInterrupt](https://docs.python.jp/3/library/exceptions.html#KeyboardInterrupt)のリンク先を見る。

> ユーザが割り込みキー (通常は Control-C または Delete) を押した場合に送出されます。

Deleteキー押下するも`^[[3~`と表示されるだけで[KeyboardInterrupt](https://docs.python.jp/3/library/exceptions.html#KeyboardInterrupt)例外は発生しない。Enterキーで確定すると、コードにある通り`Valueerror`時のエラーメッセージが表示される。

### 説明コードではキャッチしていない

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again")
```

そもそも、この例のコードでは、`int()`で数値変換できなかったことによる`ValueError`をキャッチしているように見える。[KeyboardInterrupt](https://docs.python.jp/3/library/exceptions.html#KeyboardInterrupt)例外はキャッチしていない。なぜ唐突に[KeyboardInterrupt](https://docs.python.jp/3/library/exceptions.html#KeyboardInterrupt) 例外とやらが出てきたのか。

### コードを書いて確かめたが発生せず

念の為、コードを以下のようにして`KeyboardInterrupt`のキャッチを追加した。`Ctrl+C`キー押下しても無反応だし、`Delete`キー押下しても`^[[3~`と表示されるだけで無反応。その状態でEnterキー押下すると`ValueError`のメッセージが表示される。`KeyboardInterrupt`が発生した様子はない。

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except KeyboardInterrupt:
        print("KeyboardInterrupt!!")
    except ValueError:
        print("Oops!  That was no valid number.  Try again")
```
```sh
$ python 1.py 
Please enter a number: ^[[3~
Oops!  That was no valid number.  Try again
Please enter a number: 
```

## 謎まとめ

* [KeyboardInterrupt](https://docs.python.jp/3/library/exceptions.html#KeyboardInterrupt) 例外とは何なのか
* 各OSでそれを発生させるにはどうすればいいのか
    * それをどうやって調べればいいのか

