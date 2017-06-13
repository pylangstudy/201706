with open('some.txt', mode='w', encoding='utf-8') as f:
    f.write('ABC')
with open('some.txt', mode='r', encoding='utf-8') as f:
    print(f.read())

