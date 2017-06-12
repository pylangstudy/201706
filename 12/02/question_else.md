# tryにおけるelse節の利用価値はあるのか？

[8.3. 例外を処理する](https://docs.python.jp/3/tutorial/errors.html#handling-exceptions) < [8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html#errors-and-exceptions) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 無いと思う

> 追加のコードを追加するのは try 節の後ろよりも else 節の方がよいでしょう。なぜなら、そうすることで try ... except 文で保護したいコードから送出されたもの以外の例外を偶然に捕捉してしまうという事態を避けられるからです。

else節の中でtryしたくなったらネストが深くなっていきそうなのだが……。素直に`else`を使わず、try文から完全に抜けて書けばいいだけなのでは？

else節、使う価値があるのだろうか。利用場面が思いつかないので使わないでおこう。

finallyなら欲しい。exceptで強制終了(`raise`, `return`)するパターンともみ消して継続パターンが混在し、なおかつ成功でもエラーでも同一の終了処理がしたい場合に重宝する。各箇所すべてに同一の終了処理を書かねばならない事態を回避できる。

