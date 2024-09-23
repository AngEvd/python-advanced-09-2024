rows, columns = map(int, input().split(", "))

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

for col in range(columns):
    column_sum = 0
    for row in range(rows):
        column_sum += matrix[row][col]
    print(column_sum)