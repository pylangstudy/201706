class Human:
    def walk(self):
        print('walk.')
class Programmer(Human):
    def walk(self):
        super().walk()
        Human.walk(self)
        print('smart walk.')

p = Programmer()
print('プログラマは人間から派生したものか？:', issubclass(Programmer, Human))
print('人間はプログラマから派生したものか？:', issubclass(Human, Programmer))
print('数値は人間から派生したものか？:', issubclass(int, Human))
