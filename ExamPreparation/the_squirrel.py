from collections import deque

size = int(input())
directions = deque(input().split(", "))

matrix = []
squirrel = (None, None)
fail = False
hazelnuts = 0

for row in range(size):
    row_data = [char for char in input()]
    if "s" in row_data:
        squirrel = (row, row_data.index("s"))
    matrix.append(row_data)

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while directions:
    row, col = moves[directions.popleft()]
    new_row = squirrel[0] + row
    new_col = squirrel[1] + col
    if not (0 <= new_row < size and 0 <= new_col < size):
        print("The squirrel is out of the field.")
        fail = True
        break

    next_cell = matrix[new_row][new_col]
    matrix[squirrel[0]][squirrel[1]] = "*"
    squirrel = (new_row, new_col)

    if next_cell == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        fail = True
        break
    elif next_cell == "h":
        hazelnuts += 1
    else:
        continue

if not fail:
    if hazelnuts < 3:
        print("There are more hazelnuts to collect.")
    else:
        print("Good job! You have collected all hazelnuts!")
print(f"Hazelnuts collected: {hazelnuts}")
