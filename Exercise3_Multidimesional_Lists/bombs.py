rows = int(input())

matrix = []
flat_matrix = []
matrix_sum = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

bomb_coordinates = [[int(x), int(y)] for x, y in (pair.split(",") for pair in input().split())]

for bomb in bomb_coordinates:
    row, col = bomb
    explosion_power = matrix[row][col]

    if explosion_power > 0:
        matrix[row][col] = 0
        min_row = max(0, row - 1)
        max_row = min(len(matrix) - 1, row + 1)
        min_col = max(0, col - 1)
        max_col = min(len(matrix) - 1, col + 1)

        for r in range(min_row, max_row + 1):
            for c in range(min_col, max_col + 1):
                if (r, c) != (row, col) and matrix[r][c] > 0:
                    matrix[r][c] -= explosion_power

for row in range(rows):
    flat_matrix.extend(matrix[row])

alive_cells = list(filter(lambda x: x > 0, flat_matrix))

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in range(rows):
    print(*matrix[row])
