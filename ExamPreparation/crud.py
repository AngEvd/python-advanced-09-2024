matrix = []

for _ in range(6):
    matrix.append(input().split())

start_position = [int(x) for x in input() if x.isdigit()]

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
value = None

while True:
    user_input = input()
    if user_input == "Stop":
        break
    else:
        cmd_lines = user_input.split(", ")
        command = cmd_lines[0]
        direction = cmd_lines[1]
        if len(cmd_lines) == 3:
            value = cmd_lines[2]

    next_row = int(start_position[0]) + moves[direction][0]
    next_col = int(start_position[1]) + moves[direction][1]
    next_cell = matrix[next_row][next_col]

    if command == "Create" and next_cell == ".":
        matrix[next_row][next_col] = value
    elif command == "Update" and next_cell != ".":
        matrix[next_row][next_col] = value
    elif command == "Delete" and next_cell != ".":
        matrix[next_row][next_col] = "."
    elif command == "Read" and next_cell != ".":
        print(next_cell)

    start_position = [next_row, next_col]

[print(*row) for row in matrix]




