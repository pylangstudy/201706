class Human:
    def walk(self):
        print('walk.')
class Programmer(Human):
    def walk(self):
        super().walk()
        Human.walk(self)
        print('smart walk.')

p = Programmer()
p.walk()
