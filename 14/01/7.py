class MyClass:
    class_var = 'class_var'
    def __init__(self):
        self.instance_var = 'instance_var'
    def instance_method(self):
        print('instance_method:', self.instance_var)
#        print(class_var) # NameError: name 'class_var' is not defined
        print(self.class_var) # NameError: name 'class_var' is not defined
    @classmethod
    def class_method(cls):
        print('class_method:', cls.class_var)
    @staticmethod
    def static_method():
        print('static_method')

if __name__ == '__main__':
    c = MyClass()
    c.instance_method()
    c.class_method()
    MyClass.static_method()
