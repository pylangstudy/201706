class Human:
    def __init__(self):
        self.name = 'name'
        self._name = '_name'
        self.__name = '__name'

he = Human()
print(he.name)
print(he._name)
print(he._Human__name)

