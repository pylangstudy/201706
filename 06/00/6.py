d = {'Key3': 'A', 'Key2': 'B', 'Key1': 'C'}
for key in sorted(d.keys()):
    print(key, d[key])
for value in sorted(d.values()):
    print(value, [k for k,v in d.items() if value == v][0])

