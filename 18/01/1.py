class Human:
    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name
    def intro(self):
        print(self.get_serif())
    def get_serif(self):
        return 'My name is ' + self.first_name + ' ' + self.last_name + ' .'

taro = Human('太郎', '山田')
ichiro = Human('一郎', '鈴木')
taro.intro()
ichiro.intro()

