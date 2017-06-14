class MyParent:
    def parent_method(self):
        print('base_method')
class MyChild(MyParent):
    def child_method(self):
        print('child_method call: ', end='')
        self.parent_method()

if __name__ == '__main__':
    c = MyChild()
    c.parent_method()
    c.child_method()
