rows = int(input())

matrix = []
diagonal_sum = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

row = 0
for col in range(rows - 1, -1, -1):
    diagonal_sum += matrix[row][col]
    row += 1

print(diagonal_sum)
