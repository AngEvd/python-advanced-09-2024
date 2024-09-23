rows, columns = map(int, input().split(" "))

matrix = []
maximal_sum = 0

sub_matrix = [[], [], []]

for row in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

for row in range(1, rows - 1):
    for col in range(1, columns - 1):
        sub_matrix_sum = matrix[row - 1][col - 1] + matrix[row - 1][col] + matrix[row - 1][col + 1] \
                         + matrix[row][col - 1] + matrix[row][col] + matrix[row][col + 1] \
                         + matrix[row + 1][col - 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]

        if sub_matrix_sum >= maximal_sum:
            sub_matrix = [[], [], []]
            maximal_sum = sub_matrix_sum
            sub_matrix[0].extend([matrix[row - 1][col - 1], matrix[row - 1][col], matrix[row - 1][col + 1]])
            sub_matrix[1].extend([matrix[row][col - 1], matrix[row][col], matrix[row][col + 1]])
            sub_matrix[2].extend([matrix[row + 1][col - 1], matrix[row + 1][col], matrix[row + 1][col + 1]])

print(f"Sum = {maximal_sum}")
for row in range(3):
    print(*sub_matrix[row])
