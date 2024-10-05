size = int(input())

matrix, fisherman = [], []
catch = 0
QUOTA = 20

for row in range(size):
    row_data = [char for char in input()]
    if "S" in row_data:
        fisherman = (row, row_data.index("S"))
    matrix.append(row_data)

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()
    if command == "collect the nets":
        break
    row, col = moves[command]
    new_row = (fisherman[0] + row) % size
    new_col = (fisherman[1] + col) % size
    if 0 <= new_row < size and 0 <= new_col < size:
        next_cell = matrix[new_row][new_col]
        if next_cell == "W":
            catch = 0
            exit(print(f"\nYou fell into a whirlpool! The ship sank and you lost the fish you caught."
                 f" Last coordinates of the ship: [{new_row},{new_col}]"))
        elif next_cell.isdigit():
            catch += int(next_cell)
        matrix[fisherman[0]][fisherman[1]] = "-"
        matrix[new_row][new_col] = "S"
        fisherman = (new_row, new_col)


if catch >= QUOTA:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA - catch} tons of fish more.")

if catch > 0:
    print(f"Amount of fish caught: {catch} tons.")

for row in matrix:
    print(*row, sep="")





