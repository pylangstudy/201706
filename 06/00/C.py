l = [100, 200, 300]
res = []
for i, item in enumerate(l):
    if i == 0: res.insert(0, 10)
    res.append(item)
print(res)
