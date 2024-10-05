size = int(input())

matrix, submarine_position = [], []
cruisers, hits = 0, 0

for row in range(size):
    row_data = [char for char in input()]
    matrix.append(row_data)
    if "S" in row_data:
        submarine_position = [row, row_data.index("S")]
    cruisers += row_data.count("C")

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while cruisers:
    command = input()
    new_row = submarine_position[0] + moves[command][0]
    new_col = submarine_position[1] + moves[command][1]
    next_cell = matrix[new_row][new_col]

    matrix[new_row][new_col] = "S"
    matrix[submarine_position[0]][submarine_position[1]] = "-"
    submarine_position = [new_row, new_col]

    if next_cell == "*":
        hits += 1
        if hits == 3:
            print(f"Mission failed, U-9 disappeared!"
                  f" Last known coordinates [{new_row}, {new_col}]!")
            break
    elif next_cell == "C":
        cruisers -= 1


else:
    print(f"Mission accomplished,"
          f" U-9 has destroyed all battle cruisers of the enemy!")

[print(*row, sep="") for row in matrix]
