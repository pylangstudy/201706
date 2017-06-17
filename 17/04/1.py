class MyClass:
    def __init__(self, var):
        self.var = var
    def method(self):
        print('var =', self.var)
    
a = MyClass('a')
b = MyClass('b')
a.method()
b.method()
MyClass.method(a)
MyClass.method(b)
MyClass.method(*[a])
# TypeError: method() takes 1 positional argument but 2 were given
#a.method(a)
#b.method(b)
#a.method(b)
#b.method(a)

