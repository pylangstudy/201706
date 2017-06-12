try:
    raise Exception('引数1', '引数2')
except Exception as e:
    print(type(e))
    print(e)
    print(e.args)
