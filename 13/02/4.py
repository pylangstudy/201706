try:
    print('try')
    raise Exception('try内で例外発生！')
except Exception as e:
    print('except')
    raise Exception('except内で例外発生！')
else:
    print('else')
finally:
    print('finally')

