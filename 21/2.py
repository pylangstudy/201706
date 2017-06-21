class MyClass:
    def method(self):
        print('method')

c = MyClass()
print(c.method) # インスタンスのメソッドオブジェクト
print(c.method.__self__) # インスタンスのクラスオブジェクト
print(c.method.__func__) # インスタンスメソッドオブジェクトの関数オブジェクト

