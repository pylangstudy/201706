class Human:
    def __init__(self, name='none_name'):
        if None is name or 0 == len(name.strip()): self.name = 'none_name'
        else: self.name = name
        self.name = ''
    def walk(self):
        print('walk.')
class Programmer(Human):
    def __init__(self, name='none_name', skills=None):
        super().__init__(name=name)
        if isinstance(skills, list):
            self.skills = skills
    def programming(self):
        print('programming.')

p = Programmer(skills=['C','C++','C#','Python','JavaScript','HTML','CSS'])
p.walk()
p.programming()
print('My name is', p.name)
print('My skill is', p.skills)
