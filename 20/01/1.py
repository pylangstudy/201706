class Human:
    def __init__(self): self.__intro()
    def intro(self): print('Human')
    __intro = intro
    def show(self): self.__intro()
class Programmer(Human):
    def intro(self): print('Programmer')

p = Programmer()
p.intro()
p.show()
