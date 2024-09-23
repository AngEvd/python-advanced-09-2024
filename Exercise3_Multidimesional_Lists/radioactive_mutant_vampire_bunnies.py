from collections import deque

rows, columns = map(int, input().split())

matrix = []
start_position = []

win = False
alive = True

for row in range(rows):
    matrix.append([char for char in input()])
    if "P" in matrix[row]:
        start_position.extend([row, matrix[row].index("P")])

commands = deque(char for char in input())

while alive and not win:
    row, col = start_position
    current_position = [row, col]
    new_position = []
    direction = commands.popleft()

    if direction == "U":
        new_position = [row - 1, col]
    elif direction == "D":
        new_position = [row + 1, col]
    elif direction == "R":
        new_position = [row, col + 1]
    elif direction == "L":
        new_position = [row, col - 1]

    if new_position:
        new_row, new_col = new_position
        matrix[row][col] = "."

        if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= columns:
            win = True
            start_position = [row, col]
        elif matrix[new_row][new_col] == "B":
            alive = False
            start_position = [new_row, new_col]
        else:
            start_position = [new_row, new_col]
            matrix[new_row][new_col] = "P"

    new_bunny_positions = []
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == "B":
                if r > 0:
                    new_bunny_positions.append([r - 1, c])
                if r < rows - 1:
                    new_bunny_positions.append([r + 1, c])
                if c > 0:
                    new_bunny_positions.append([r, c - 1])
                if c < columns - 1:
                    new_bunny_positions.append([r, c + 1])

    for r, c in new_bunny_positions:
        matrix[r][c] = "B"

    if alive and not win and matrix[start_position[0]][start_position[1]] == "B":
        alive = False

for row in range(rows):
    print(*matrix[row], sep="")

if win:
    print(f"won: {start_position[0]} {start_position[1]}")
else:
    print(f"dead: {start_position[0]} {start_position[1]}")