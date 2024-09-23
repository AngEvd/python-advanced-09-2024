from collections import deque

rows = int(input())
directions = deque(input().split())

matrix = []
start_position = []
coal = 0

for row in range(rows):
    matrix.append(input().split())
    coal += matrix[row].count("c")
    if "s" in matrix[row]:
        start_position.extend([row, matrix[row].index("s")])

while directions:
    row, col = start_position
    current_position = [row, col]
    new_position = []

    direction = directions.popleft()

    if direction == "up" and row > 0:
        new_position = [row - 1, col]

    elif direction == "down" and row < len(matrix) - 1:
        new_position = [row + 1, col]

    elif direction == "right" and col < len(matrix) - 1:
        new_position = [row, col + 1]

    elif direction == "left" and col > 0:
        new_position = [row, col - 1]

    if new_position:
        new_row, new_col = new_position
        matrix[row][col] = "*"

        if matrix[new_row][new_col] == "c":
            coal -= 1
            matrix[new_row][new_col] = "s"
            start_position = [new_row, new_col]
            if coal == 0:
                print(f"You collected all coal! ({new_row}, {new_col})")
                exit()

        elif matrix[new_row][new_col] == "e":
            print(f"Game over! ({new_row}, {new_col})")
            exit()

        else:
            matrix[new_row][new_col] = "s"
            start_position = [new_row, new_col]
else:
    print(f"{coal} pieces of coal left. ({start_position[0]}, {start_position[1]})")
