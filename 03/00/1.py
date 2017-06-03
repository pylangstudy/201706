matrix = [[1,2,3],[4,5,6]]
result = []
for i in range(3):
    result.append([row[i] for row in matrix])
print(result)
