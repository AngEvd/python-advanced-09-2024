size = int(input())

matrix = []
player_position = []
player_health = 100

for row in range(size):
    row_data = [char for char in input()]
    matrix.append(row_data)
    if "P" in row_data:
        player_position = [row, row_data.index("P")]

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    move = input()
    row, col = moves[move]
    new_row = player_position[0] + row
    new_col = player_position[1] + col
    if 0 <= new_row < size and 0 <= new_col < size:
        next_cell = matrix[new_row][new_col]
        if next_cell == "M":
            player_health = max(0, player_health - 40)
            if player_health == 0:
                print("Player is dead. Maze over!")
                matrix[new_row][new_col] = "P"
                matrix[player_position[0]][player_position[1]] = "-"
        elif next_cell == "H":
            player_health = min(100, player_health + 15)
        elif next_cell == "X":
            print("Player escaped the maze. Danger passed!")
            matrix[new_row][new_col] = "P"
            matrix[player_position[0]][player_position[1]] = "-"

        matrix[new_row][new_col] = "P"
        matrix[player_position[0]][player_position[1]] = "-"
        player_position = [new_row, new_col]

        if player_health == 0 or next_cell == "X":
            break

print(f"Player's health: {player_health} units")
[print(*row, sep="") for row in matrix]
