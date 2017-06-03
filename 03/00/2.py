matrix = [[1,2,3],[4,5,6]]
result = []
for i in range(3):
    result_row = []
    for row in matrix:
        result_row.append(row[i])
    result.append(result_row)
print(result)

