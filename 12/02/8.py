def fails():
    x = 1 / 0

try:
    fails()
except Exception as e:
    print(type(e))
    print(e)
    print(e.args)
