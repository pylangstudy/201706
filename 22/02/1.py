l = [1,2,3]
for v in (l[i] for i in range(len(l)-1, -1, -1)): print(v, end=' ')
