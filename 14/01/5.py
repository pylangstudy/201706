class MyClass:
    def my_method(self):
        print('base_method')

if __name__ == '__main__':
    c = MyClass()
    c.new_public = 'new_public'
    print(c.new_public)
    
#    c.__new_private = 'new_private'
#    print(c.__new_private) # AttributeError: 'MyClass' object has no attribute '_MyClass__new_private'
#    print(c._MyClass__new_private) # AttributeError: 'MyClass' object has no attribute '_MyClass__new_private'

    c._MyClass__new_private = 'new_private'
    print(c._MyClass__new_private)
#    print(c.__new_private) # AttributeError: 'MyClass' object has no attribute '__new_private'

