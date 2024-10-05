size = int(input())

matrix = []
money = 100
gambler = ()
jackpot = False

for row in range(size):
    row_data = [char for char in input()]
    if "G" in row_data:
        gambler = (row, row_data.index("G"))
    matrix.append(row_data)

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
cell_values = {"W": 100, "P": -200, "J": 10000, "-": 0}

while money > 0:
    command = input()
    if command == "end":
        break
    row, col = moves[command]
    new_row = gambler[0] + row
    new_col = gambler[1] + col
    if 0 <= new_row < size and 0 <= new_col < size:
        next_cell = matrix[new_row][new_col]

        matrix[new_row][new_col] = "G"
        matrix[gambler[0]][gambler[1]] = "-"
        gambler = (new_row, new_col)
        money += cell_values[next_cell]

        if next_cell == "J":
            jackpot = True
            break
    else:
        money = 0

else:
    loose = True
    exit(print("Game over! You lost everything!"))

if jackpot:
    print("You win the Jackpot!")
print(f"End of the game. Total amount: {money}$")
[print(*row, sep="") for row in matrix]
