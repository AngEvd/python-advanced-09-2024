rows, columns = map(int, input().split(", "))

matrix = []
biggest_sum = 0

sub_matrix = [[], []]

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row in range(rows - 1):
    for col in range(columns - 1):
        sub_matrix_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if sub_matrix_sum > biggest_sum:
            sub_matrix = [[], []]
            biggest_sum = sub_matrix_sum
            sub_matrix[0].extend([matrix[row][col], matrix[row][col + 1]])
            sub_matrix[1].extend([matrix[row + 1][col], matrix[row + 1][col + 1]])

for row in range(2):
    print(*sub_matrix[row])
print(biggest_sum)
