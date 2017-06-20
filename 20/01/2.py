class Human:
    def __init__(self): self.intro()
    def intro(self): print('Human')
    def show(self): self.intro()
class Programmer(Human):
    def intro(self): print('Programmer')

p = Programmer()
p.intro()
p.show()
