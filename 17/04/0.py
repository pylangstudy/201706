class MyClass:
    def __init__(self):
        self.var = 'var'
    def method(self):
        print('method')
    
x = MyClass()
x.method()

m = x.method
m()
