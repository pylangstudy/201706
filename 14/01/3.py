class MyParent:
    def parent_method(self):
        print('base_method')
class MyChild(MyParent):
    def parent_method(self):
        print('child_method call: ', end='')
        super().parent_method()
        # selfで呼び出すとMyChild.parent_methodが呼び出されて無限再帰してしまう。
#        self.parent_method() # RuntimeError: maximum recursion depth exceeded while calling a Python object

if __name__ == '__main__':
    c = MyChild()
    c.parent_method()
