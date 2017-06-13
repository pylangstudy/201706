try:
    print('try')
    raise Exception
except Exception as e:
    print('except')
finally:
    print('finally')

