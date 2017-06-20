class Human:
    def __init__(self): self.__intro()
    def intro(self): print('Human')
    __intro = intro
    def show_human(self): self.__intro()
class Programmer(Human):
    def __init__(self):
#        super().__init__()
        # ----- Human.__introを上書きする -----
        # 親クラスインスタンスの関数オブジェクトが参照できない
#        super().__intro = __intro # NameError: name '_Programmer__intro' is not defined
#        super()._Human__intro = self.intro # AttributeError: 'super' object has no attribute 'intro'
#        super()._Human__intro = __intro # NameError: name '_Programmer__intro' is not defined
#        self._Human__intro = intro # NameError: name 'intro' is not defined
#        self.__intro = self.intro # p.show_human() とすると Human.__intro でなく Programmer.intro が実行される
        print(self._Human__intro)
        print(self.intro)
        self._Human__intro = self.intro # p.show_human() とすると Human.__intro でなく Programmer.intro が実行される
    def intro(self):
        super().intro()
        print('Programmer')
#    __intro = intro
#    super().intro = intro # RuntimeError: super(): no arguments
#    _Human__intro = intro
        
p = Programmer()
p.intro()
p.show_human()
