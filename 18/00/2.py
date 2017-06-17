class Human:
    count = 0
    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name
        Human.count += 1
    def intro(self):
        print('私の名前は', self.last_name, self.first_name, 'です。')
    def all_number():
        print('全人類数:', Human.count)

taro = Human('太郎', '山田')
ichiro = Human('一郎', '鈴木')
taro.intro()
ichiro.intro()
Human.all_number()

