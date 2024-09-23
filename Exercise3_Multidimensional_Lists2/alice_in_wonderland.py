size = int(input())

matrix = []
alice_position = []
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
tea_bags = 0

for row in range(size):
    row_data = [x for x in input().split()]
    matrix.append(row_data)
    if "A" in row_data:
        alice_position = [row, row_data.index("A")]

while tea_bags < 10:
    direction = input()
    row_move, col_move = possible_moves[direction]
    next_row = alice_position[0] + row_move
    next_col = alice_position[1] + col_move
    if not (0 <= next_row < size and 0 <= next_col < size):
        matrix[alice_position[0]][alice_position[1]] = "*"
        break
    elif matrix[next_row][next_col] == "R":
        matrix[alice_position[0]][alice_position[1]] = "*"
        matrix[next_row][next_col] = "*"
        break
    else:
        matrix[alice_position[0]][alice_position[1]] = "*"
        if matrix[next_row][next_col] not in "*.":
            tea_bags += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = "*"
        alice_position = [next_row, next_col]

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]
