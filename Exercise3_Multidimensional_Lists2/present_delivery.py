presents = int(input())
hood_size = int(input())

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
adj_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
matrix = []
santa_position = []
good_kids = 0
happy_kids = 0

for row in range(hood_size):
    row_data = input().split()
    if "S" in row_data:
        santa_position = [row, row_data.index("S")]
    if "V" in row_data:
        good_kids += row_data.count("V")
    matrix.append(row_data)

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    else:
        new_row = santa_position[0] + directions[command][0]
        new_col = santa_position[1] + directions[command][1]

        if 0 <= new_row < hood_size and 0 <= new_col < hood_size:
            if matrix[new_row][new_col] == "V":
                good_kids -= 1
                happy_kids += 1
                presents -= 1
            elif matrix[new_row][new_col] == "C":
                for direction in adj_directions:
                    new_r = new_row + direction[0]
                    new_c = new_row + direction[1]
                    if 0 <= new_r < hood_size and 0 <= new_c < hood_size and matrix[new_r][new_c] in "XV":
                        if matrix[new_r][new_c] == "V":
                            good_kids -= 1
                            happy_kids += 1
                        matrix[new_r][new_c] = "-"
                        presents -= 1

        matrix[new_row][new_col] = "S"
        matrix[santa_position[0]][santa_position[1]] = "-"
        santa_position = [new_row, new_col]

if presents <= 0 and good_kids > 0:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if good_kids == 0:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids} nice kid/s.")
