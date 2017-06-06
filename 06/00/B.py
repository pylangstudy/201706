l = [100, 200, None, 300]
res = []
for i, item in enumerate(l):
    if None is not item: res.append(item)
print(res)
