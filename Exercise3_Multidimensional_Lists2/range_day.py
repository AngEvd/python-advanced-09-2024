size = 5
matrix = []
start_position = []
targets, hits = 0, 0
targets_hit = []
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(size):
    row_data = input().split()
    if "A" in row_data:
        start_position = [row, row_data.index("A")]
    if "x" in row_data:
        targets += row_data.count("x")
    matrix.append(row_data)

for _ in range(int(input())):
    command = input().split()
    direction = command[1]
    row_move, col_move = directions[direction]
    if command[0] == "move":
        steps = int(command[2])
        row = start_position[0] + row_move * steps
        col = start_position[1] + col_move * steps
        if 0 <= row < size and 0 <= col < size and matrix[row][col] == ".":
            matrix[row][col] = "A"
            matrix[start_position[0]][start_position[1]] = "."
            start_position = [row, col]
    elif command[0] == "shoot":
        row = start_position[0] + row_move
        col = start_position[1] + col_move

        while 0 <= row < size and 0 <= col < size:
            if matrix[row][col] == "x":
                targets -= 1
                hits += 1
                matrix[row][col] = "."
                targets_hit.append([row, col])
                break
            else:
                row += row_move
                col += col_move
        if targets == 0:
            print(f"Training completed! All {hits} targets hit.")
            break

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
print(*targets_hit, sep="\n")
