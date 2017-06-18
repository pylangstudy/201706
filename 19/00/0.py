class Human:
    def walk(self):
        print('walk.')
class Programmer(Human):
    def programming(self):
        print('programming.')

p = Programmer()
p.walk()
p.programming()
