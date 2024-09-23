rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([char for char in input()])

possible_moves = (
    (-1, -2,), (1, -2),
    (-2, -1), (2, -1),
    (-2, 1), (2, 1),
    (-1, 2), (1, 2)
)

removed_knights = 0

while True:
    max_attacks = 0
    most_attacks_knight = []

    for row in range(rows):
        for col in range(rows):
            if matrix[row][col] == "K":
                attacks = 0
                for move in possible_moves:
                    move_row = row + move[0]
                    move_col = col + move[1]

                    if 0 <= move_row < rows and 0 <= move_col < rows:
                        if matrix[move_row][move_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    most_attacks_knight = [row, col]
                    max_attacks = attacks

    if most_attacks_knight:
        r, c = most_attacks_knight
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
