try:
    print('try')
    pass
except SyntaxError:
    print('SyntaxError')
except (ValueError, NameError):
    print('ValueError, NameError')
except:
    print('except')
    raise
else:
    print('else')
