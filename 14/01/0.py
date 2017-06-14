class MyClass:
    def __init__(self):
        self.__private = 'private'
        self.public = 'public'

if __name__ == '__main__':
    c = MyClass()
    print(c.public)
#    print(c.__private) # AttributeError: 'MyClass' object has no attribute '__private'
    print(c._MyClass__private)
