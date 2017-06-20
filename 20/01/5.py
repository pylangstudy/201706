class Human:
#    def __init__(self): self.__intro()
    def intro(self): print('Human')
#    __intro = intro
#    def show_human(self): self.__intro()
class Programmer(Human):
#    def __init__(self): self.__intro()
    def intro(self):
        super().intro()
        print('Programmer')
#    __intro = intro
#    def show_programmer(self): self.__intro()
class Engineer(Programmer):
#    def __init__(self): self.__intro()
    def intro(self):
        super().intro()
        print('Engineer')
#    __intro = intro

#p = Programmer()
#p.intro()
e = Engineer()
e.intro()
#e.show_programmer()
