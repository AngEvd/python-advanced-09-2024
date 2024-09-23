rows = int(input())

matrix = []
diagonal_sum = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

for row in range(rows):
    diagonal_sum += matrix[row][row]

print(diagonal_sum)
