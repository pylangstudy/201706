try:
    f = open('some.txt', mode='r', encoding='utf-8')
    print(f.read())
finally:
    f.close()

