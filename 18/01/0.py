def intro(self):
    print('私の名前は', self.name, 'です。')

class Human:
    def __init__(self, name):
        self.name = name
    intro = intro

taro = Human('太郎')
ichiro = Human('一郎')
taro.intro()
ichiro.intro()

