with open('some.txt', 'w') as f:
    f.write('Write!!')
with open('some.txt') as f:
    print(f.read())

