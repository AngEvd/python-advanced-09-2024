rows, columns = map(int, input().split(", "))

matrix = []
matrix_sum = 0

for row in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)
    matrix_sum += sum(row_data)

print(matrix_sum)
print(matrix)
