n, m = map(int, input().split(","))

matrix = []
mouse = (None, None)
cheese = 0


for row in range(n):
    row_data = [char for char in input()]
    if "M" in row_data:
        mouse = (row, row_data.index("M"))
    cheese += row_data.count("C")
    matrix.append(row_data)

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break
    row, col = moves[command]
    new_row = mouse[0] + row
    new_col = mouse[1] + col

    if not (0 <= new_row < n and 0 <= new_col < m):
        print("No more cheese for tonight!")
        break

    next_cell = matrix[new_row][new_col]

    if next_cell == "@":
        continue

    matrix[mouse[0]][mouse[1]] = "*"
    matrix[new_row][new_col] = "M"
    mouse = (new_row, new_col)

    if next_cell == "T":
        print("Mouse is trapped!")
        break
    elif next_cell == "C":
        cheese -= 1
        if cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

[print(*row, sep="") for row in matrix]
