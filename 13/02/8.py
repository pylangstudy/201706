def func():
    for i in [0, 1, 2]:
        try:
            print('try    「yieldだ、別れよう」'.format(i))
            yield
        finally:
            print('finally「私を捨てるの？させないわ」')

for i in func():
    pass
print('The End.')
