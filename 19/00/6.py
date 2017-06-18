class Human:
    def walk(self):
        print('walk.')
class Programmer(Human):
    def walk(self):
        super().walk()
        Human.walk(self)
        print('smart walk.')

p = Programmer()
print('プログラマAは人間の型から生成されたか？:', isinstance(p, Human))
print('人間Aはプログラマの型から生成されたか？:', isinstance(Human(), Programmer))
print('整数値100はHumanの型から生成されたか？:', isinstance(100, Human))
