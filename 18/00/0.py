class Human:
    last_name = 'ラストネーム'
    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        last_name = _last_name
#        nonlocal last_name
#        global last_name
#    def intro(self):
#        print('My name is', self.__first_name, __last_name)

taro = Human('太郎', '山田')
print('My name is {0} {1}'.format(taro.first_name, taro.last_name))
#taro.intro()
ichiro = Human('一郎', '鈴木')
print('My name is', ichiro.first_name, ichiro.last_name)
#ichiro.intro()
#taro.intro()
