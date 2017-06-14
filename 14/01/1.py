class MyParent:
    def __init__(self):
        self.__private = 'private'
        self.public = 'public'
    
class MyChild(MyParent):
    def __init__(self):
        super().__init__()
    def Show(self):
        print(self.public)
        # protectedで子クラスにだけ参照させることができない。
#        print(self.__private) # AttributeError: 'MyChild' object has no attribute '_MyChild__private'
#        print(self._MyClass__private) # AttributeError: 'MyChild' object has no attribute '_MyChild__private'
#        print(super().__private) # AttributeError: 'super' object has no attribute '_MyChild__private'
#        print(super()._MyClass__private) # AttributeError: 'super' object has no attribute '_MyClass__private'

if __name__ == '__main__':
    cc = MyChild()
    cc.Show()
