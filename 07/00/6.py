def check(s):
    if None is s or 0 == len(s):
        print('文字列 s は None または 空文字 です。')
    else:
        print(s)
check('')
check(None)
check('abcdefg')
