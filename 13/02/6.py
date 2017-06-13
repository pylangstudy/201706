def func():
    for i in [0, 1, 2]:
        try:
            print('try    「continueで変質者finallyから逃げるわ！({0}回目)」'.format(i))
            continue
        finally:
            print('finally「逃がないよtryちゃん （；´Д`）ﾊｧﾊｧ」')

func()
print('The End.')
