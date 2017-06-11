d = [{'name': 'Yamada', 'age': 123}, {'name': 'Takahashi', 'age': 88}]
for record in d:
    print('{0[name]:12s}|{0[age]:4d}'.format(record))
