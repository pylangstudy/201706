class MyClass:
    def __init__(self, name):
        self.__name = name
    def Show(self):
        print(self.__name)
c1 = MyClass('c1')
c2 = MyClass('c2')
c3 = MyClass('c3')
c4 = MyClass('c4')
a = {x.Show() for x in {c1, c2, c3, c4} if x not in {c1, c2}}
