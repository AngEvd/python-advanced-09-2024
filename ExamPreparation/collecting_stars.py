size = int(input())

matrix = []
player_position = []
stars = 2

for row in range(size):
    row_data = input().split()
    matrix.append(row_data)
    if "P" in row_data:
        player_position = [row, row_data.index("P")]

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while 0 < stars < 10:
    move = input()
    row, col = moves[move]
    new_row = player_position[0] + row
    new_col = player_position[1] + col
    if 0 <= new_row < size and 0 <= new_col < size:
        if matrix[new_row][new_col] == "#":
            stars -= 1
        else:
            if matrix[new_row][new_col] == "*":
                stars += 1
            matrix[new_row][new_col] = "P"
            matrix[player_position[0]][player_position[1]] = "."
            player_position = [new_row, new_col]
    else:
        matrix[player_position[0]][player_position[1]] = "."
        player_position = [0, 0]
        if matrix[0][0] == "*":
            stars += 1
        matrix[0][0] = "P"

if stars == 10:
    print("You won! You have collected 10 stars.")
elif stars == 0:
    print("Game over! You are out of any stars.")
print(f"Your final position is {player_position}")
[print(*row) for row in matrix]
