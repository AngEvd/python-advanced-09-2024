rows, columns = map(int, input().split(" "))

matrix = []
squares = 0

sub_matrix = [[], []]

for row in range(rows):
    matrix.append(input().split(" "))

for row in range(rows - 1):
    for col in range(columns - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            squares += 1

print(squares)