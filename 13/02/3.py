try:
    print('try')
except Exception as e:
    print('except')
else:
    print('else')
    raise Exception('else内で例外発生！')
finally:
    print('finally')

