# コンピュータのデータ形式

< [ReadMe.md](https://github.com/pylangstudy/201706/blob/master/28/01/ReadMe.md)

私個人的の未熟な認識。間違いだらけかもしれない。

## コンピュータの構造

コンピュータは[メモリ](https://ja.wikipedia.org/wiki/%E4%B8%BB%E8%A8%98%E6%86%B6%E8%A3%85%E7%BD%AE)や[ディスク](https://ja.wikipedia.org/wiki/%E8%A3%9C%E5%8A%A9%E8%A8%98%E6%86%B6%E8%A3%85%E7%BD%AE)にデータを記憶する。記憶したデータを元にCPUで加算、減算などの演算を行う。その結果を出力装置などへ出す。

プログラムを実行するときはデータをディスクからメモリに移す。ディスクよりもメモリのほうが高速にアクセスできるから。ただしメモリは小容量しかないため少しずつディスクから読み取り、順次実行する。

### バイナリデータ構造

メモリやディスクにあるデータはバイナリ形式である。バイナリはbitの羅列である。bitはコンピュータにおける最小単位である。1bitは0と1の2状態を表せる。2bitなら00,01,10,11の4状態を表せる。3bitなら000,001,010,011,100,101,110,111の8状態(2**3=8)。8bitは256状態([2**8](https://www.google.co.jp/search?q=2**8&ie=utf-8&oe=utf-8&client=firefox-b&gfe_rd=cr&ei=melSWe6FH63U8AfhsZvYDg)=256)。

以下のxは1bitである。8つある(8bit)。xは0または1のいずれかの状態をとる。それらの全パターンは256ある(2の8乗)。

```
xxxxxxxx
```

一般に8bitを1Byteとする。(2Byte=16bit, 3Byte=24bit=8*3, 4Byte=32bit=8*4)

### ハードウェア構造

1bitの物理的な表現は、メモリやディスクなど構造が違う物ごとに異なる仕組みがある。たとえばメモリは[半導体](https://ja.wikipedia.org/wiki/%E5%8D%8A%E5%B0%8E%E4%BD%93%E3%83%A1%E3%83%A2%E3%83%AA)でできている。中に微小な[コンデンサ](https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%B3%E3%83%87%E3%83%B3%E3%82%B5)がある。蓄電しているときを`1`, 蓄電していないときを`0`とする。これで1bitを表す。メモリ容量が1GBなら1GB分蓄電できるものである。

## データの表現

* [DataRepresentation.md](https://github.com/pylangstudy/201706/blob/master/28/01/DataRepresentation.md)

## [バイトオーダー](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%B3%E3%83%87%E3%82%A3%E3%82%A2%E3%83%B3)

[バイトオーダー(エンディアン)](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%B3%E3%83%87%E3%82%A3%E3%82%A2%E3%83%B3)とは、バイナリデータの並び順である。

たとえば8桁の16進数値`1234ABCD`を1バイトずつ半角スペースで区切った場合、以下のようなバイト配列になる。

エンディアン|配列|説明
-----------|----|----
Big Endian|`12 34 AB CD`
Little Endian|`CD AB 34 12`

## アラインメント

アラインメントとは、メモリ空間の余白である。開始位置を2進数的にキリのよい位置にするために余白を用いる。それがアラインメントである。（たぶん）

たとえば32bitマシンなら、32bitずつメモリ確保する。たとえ実際に使うのが16bitなど32bit未満だとしても。キリのよい位置にすることでアクセス数が減らせ、実行速度を高速にできる。

http://www5d.biglobe.ne.jp/~noocyte/Programming/Alignment.html

