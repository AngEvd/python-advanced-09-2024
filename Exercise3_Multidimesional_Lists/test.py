rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

bomb_coordinates = [[int(x), int(y)] for x, y in (pair.split(",") for pair in input().split())]

# Store a copy of the original matrix to ensure bombs are not affected by other explosions
original_matrix = [row[:] for row in matrix]

for bomb in bomb_coordinates:
    row, col = bomb
    explosion_power = original_matrix[row][col]

    if explosion_power > 0:  # Only explode if the bomb has a positive power
        matrix[row][col] = 0  # Set bomb position to 0

        # Define the range for rows and columns that will be affected
        min_row = max(0, row - 1)
        max_row = min(rows - 1, row + 1)
        min_col = max(0, col - 1)
        max_col = min(len(matrix[row]) - 1, col + 1)

        # Reduce the values of adjacent cells based on the explosion power
        for r in range(min_row, max_row + 1):
            for c in range(min_col, max_col + 1):
                if (r, c) != (row, col) and matrix[r][c] > 0:  # Skip the bomb position itself
                    matrix[r][c] -= explosion_power

# Print the final matrix after all bombs explode
for row in matrix:
    print(*row)

