rows = int(input())

matrix = []


for row in range(rows):
    matrix.append([x for x in input()])

symbol = input()

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            exit()

print(f"{symbol} does not occur in the matrix")
