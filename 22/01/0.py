def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for v in reverse([1,2,3]): print(v, end=' ')
