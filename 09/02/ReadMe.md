# [6.1.1. モジュールをスクリプトとして実行する](https://docs.python.jp/3/tutorial/modules.html#executing-modules-as-scripts)

[6.1. モジュールについてもうすこし](https://docs.python.jp/3/tutorial/modules.html#more-on-modules) < [6. モジュール (module)](https://docs.python.jp/3/tutorial/modules.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## モジュールのスクリプト実行

>  import できるモジュールであると同時にスクリプトとしても使えるようになります。

> モジュールには、関数定義に加えて実行文を入れることができます。これらの実行文はモジュールを初期化するためのものです。これらの実行文は、インポート文の中で 最初に モジュール名が見つかったときにだけ実行されます。[1] (ファイルがスクリプトとして実行される場合も実行されます。)

some_module_0.py
```python
def some_method(argv):
    print('some_method():', argv)


if __name__ == '__main__':
    import sys
    some_method(sys.argv)
```
call_0.py
```python
import some_module_0
some_module_0.some_method(['some_argv'])
```
run.sh
```sh
python3 some_module_0.py some_argv123
python3 call_0.py
```
```sh
$ bash run.sh 
some_method(): ['some_module_0.py', 'some_argv123']
some_method(): ['some_argv']
```

> モジュールが “main” ファイルとして起動されたときだけ、コマンドラインを解釈するコードが実行される

> モジュールが import された場合は、そのコードは実行されません

## 用途

> この方法はモジュールに便利なユーザインターフェースを提供したり、テストのために (スクリプトをモジュールとして起動しテストスイートを実行して) 使われます。

