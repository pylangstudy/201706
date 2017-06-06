l = [100, 200, None, 300]
for i, item in enumerate(l):
    if None is item:
        del l[i]
        continue
    print(item)

