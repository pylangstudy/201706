try:
    print('try')
#    raise SyntaxError
#    raise ValueError
#    raise Exception
except SyntaxError:
    print('SyntaxError')
except (ValueError, NameError):
    print('ValueError, NameError')
except:
    print('except')
    raise
else:
    print('else')
