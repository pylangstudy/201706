class Human:
    def __init__(self): self.type_name = 'Human'
class Elf:
    def __init__(self): self.type_name = 'Elf'
class HumanElf(Human, Elf):
    def __init__(self):
#        print(super().type_name) # AttributeError: 'super' object has no attribute 'type_name'
        super().__init__()
#        print(super().type_name) # AttributeError: 'super' object has no attribute 'type_name'

he = HumanElf()
