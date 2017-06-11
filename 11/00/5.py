d = [{'name': 'Yamada', 'age': 123}, {'name': 'Takahashi', 'age': 88}]
for r in d:
    print('{name:12s}|{age:4d}'.format(**r))
