def func():
    for i in [0, 1, 2]:
        try:
            print('try    「breakでfinally子を回避！」'.format(i))
            break
        finally:
            print('finally「私から逃げられるとでも思ったの？」')

func()
print('The End.')
