class Human:
    def __init__(self): self.type_name = 'Human'
class Elf:
    def __init__(self): self.type_name = 'Elf'
class HumanElf(Human, Elf):
    def __init__(self):
#        print(self.type_name) # AttributeError: 'HumanElf' object has no attribute 'type_name'
        super().__init__()
        print(self.type_name) # Human
        self.type_name = 'HumanElf'
        print(self.type_name) # HumanElf

he = HumanElf()
