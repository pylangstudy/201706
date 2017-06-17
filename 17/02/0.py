class MyClass:
    var = 'my_class_var'
    def func():
        print('func()')

print(MyClass.var)
MyClass.func()

MyClass.var = 'after'
print(MyClass.var)
