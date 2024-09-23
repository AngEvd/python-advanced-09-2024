size = int(input())

matrix = []
max_direction = None
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
max_eggs = float("-inf")
max_eggs_matrix = []
bunny_position = []

for row in range(size):
    row_data = [x for x in input().split()]
    matrix.append(row_data)
    if "B" in row_data:
        bunny_position = [row, row_data.index("B")]

for direction, move in possible_moves.items():
    eggs = 0
    eggs_matrix = []
    row = bunny_position[0] + move[0]
    col = bunny_position[1] + move[1]

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break
        else:
            eggs += int(matrix[row][col])
            eggs_matrix.append([row, col])
            row += move[0]
            col += move[1]

    if eggs >= max_eggs:
        max_eggs = eggs
        max_eggs_matrix = eggs_matrix
        max_direction = direction

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)
