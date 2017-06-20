class Human:
    def __init__(self): self.__intro()
    def intro(self): print('Human')
    __intro = intro
class Programmer(Human):
    def intro(self):
        print('---------Programmer intro start----------')

#        super().__intro() # AttributeError: 'super' object has no attribute '_Programmer__intro'
        super()._Human__intro()
#        super()._Human__intro(self) # TypeError: intro() takes 1 positional argument but 2 were given

#        self.__intro() # AttributeError: 'Programmer' object has no attribute '_Programmer__intro'
        self._Human__intro() # プライベートメソッドも継承されているからselfで参照できる？
#        self._Human__intro(self) # TypeError: intro() takes 1 positional argument but 2 were given

        print('Programmer')
        print('---------Programmer intro end----------')

p = Programmer()
p.intro()
