rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

command = input()

while command != "END":
    arguments = command.split()
    row, col, value = map(int, arguments[1:])

    if row not in range(rows) or col not in range(rows):
        print(f"Invalid coordinates")
    else:
        if arguments[0] == "Add":
            matrix[row][col] += value
        elif arguments[0] == "Subtract":
            matrix[row][col] -= value

    command = input()

for row in range(rows):
    print(*matrix[row])
