size = int(input())

matrix = []
bee_position = []
energy = 15
nectar = 0
hive = False
restored = False

for row in range(size):
    row_data = [char for char in input()]
    matrix.append(row_data)
    if "B" in row_data:
        bee_position = [row, row_data.index("B")]

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while energy > 0:
    move = input()
    row, col = moves[move]
    new_row = (bee_position[0] + row) % size
    new_col = (bee_position[1] + col) % size
    next_cell = matrix[new_row][new_col]
    energy -= 1
    if next_cell.isdigit():
        nectar += int(next_cell)
    elif next_cell == "H":
        hive = True

    matrix[new_row][new_col] = "B"
    matrix[bee_position[0]][bee_position[1]] = "-"
    bee_position = [new_row, new_col]

    if hive:
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break
    if energy == 0:
        if nectar > 30 and not restored:
            energy += nectar - 30
            nectar = 30
            restored = True
        else:
            print("This is the end! Beesy ran out of energy.")
            break

[print(*row, sep="") for row in matrix]
