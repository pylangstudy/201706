with open('some.txt', 'w') as f:
    f.write("""one
two
three""")
with open('some.txt') as f:
    for i, line in enumerate(f):
        print(i, line, end='')
    print()

