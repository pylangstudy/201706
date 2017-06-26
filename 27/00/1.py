import reprlib
class MyList(list):
    @reprlib.recursive_repr()
    def __repr__(self):
        return '<' + '|'.join(map(repr, self)) + '>'

m = MyList('abc')
m.append(m)
m.append('x')
print(m)
