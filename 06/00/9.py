l = [100, 200, 300]
for i, item in enumerate(l):
    if i == 0: l.insert(0, 10)
    print(i, item)
print(l)
