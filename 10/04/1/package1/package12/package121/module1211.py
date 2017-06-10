#print('0/package1/package12/module121.py Run!!')
from . import module122
def some_method():
    print('module121.some_method()')
    module122.some_method()
