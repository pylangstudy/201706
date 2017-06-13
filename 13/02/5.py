def func():
    try:
        print('try     「returnで切り抜ける！」')
        return
    finally:
        print('finally 「逃がしはせんよ！」')

func()
print('The End.')
