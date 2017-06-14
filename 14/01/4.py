class MyClass:
    def my_method(self):
        print('base_method')

if __name__ == '__main__':
    c = MyClass()
    c.new_method = lambda: print('new_method')
    c.new_method()

