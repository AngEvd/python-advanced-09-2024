matrix = [[int(x) for x in input().split(" ")] for row in range(int(input()))]

primary_diagonal = []
secondary_diagonal = []

for row in range(len(matrix)):
    primary_diagonal.append(matrix[row][row])

row = 0
for col in range(len(matrix) - 1, -1, -1):
    secondary_diagonal.append(matrix[row][col])
    row += 1

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
