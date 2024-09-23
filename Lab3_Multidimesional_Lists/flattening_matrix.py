rows = int(input())

matrix = []

for row in range(rows):
    matrix.extend([int(x) for x in input().split(", ")])

print(matrix)