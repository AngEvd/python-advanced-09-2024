n, m = (map(int, input().split()))

matrix = []
player_position = []
moves_made, touched_players = 0, 0

for row in range(n):
    row_data = input().split()
    matrix.append(row_data)
    if "B" in row_data:
        player_position = (row, row_data.index("B"))

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while touched_players < 3:
    command = input()
    if command == "Finish":
        break

    new_row = player_position[0] + moves[command][0]
    new_col = player_position[1] + moves[command][1]
    if 0 <= new_row < n and 0 <= new_col < m:
        next_cell = matrix[new_row][new_col]
        if next_cell == "O":
            continue
        if next_cell == "P":
            touched_players += 1
        matrix[new_row][new_col] = "B"
        matrix[player_position[0]][player_position[1]] = "-"
        player_position = [new_row, new_col]
        moves_made += 1

print(f"Game over!\nTouched opponents: {touched_players} Moves made: {moves_made}")
