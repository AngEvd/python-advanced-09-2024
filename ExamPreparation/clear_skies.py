size = int(input())

matrix = []
armor = 300
enemies = 0
jet = ()

for row in range(size):
    row_data = [char for char in input()]
    if "J" in row_data:
        jet = (row, row_data.index("J"))
    enemies += row_data.count("E")

    matrix.append(row_data)

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()
    row, col = moves[command]
    new_row = jet[0] + row
    new_col = jet[1] + col
    if 0 <= new_row < size and 0 <= new_col < size:
        next_cell = matrix[new_row][new_col]

        matrix[new_row][new_col] = "J"
        matrix[jet[0]][jet[1]] = "-"
        jet = (new_row, new_col)

        if next_cell == "E":
            enemies -= 1
            if enemies > 0:
                armor -= 100
                if armor == 0:
                    print(f"Mission failed, your jetfighter was shot down!"
                          f" Last coordinates [{new_row}, {new_col}]!")
                    break
            else:
                print("Mission accomplished, you neutralized the aerial threat!")
                break

        elif next_cell == "R":
            armor = 300


[print(*row, sep="") for row in matrix]