rows, columns = map(int, input().split())

matrix = []

for row in range(rows):
    matrix.append(input().split())

command = input()

while command != "END":
    arguments = command.split()
    if arguments[0] != "swap" or len(arguments) != 5:
        print("Invalid input!")
    else:
        row1, col1, row2, col2 = map(int, arguments[1:])

        if row1 not in range(rows)\
                or col1 not in range(columns)\
                or row2 not in range(rows)\
                or col2 not in range(columns):
            print("Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in range(rows):
                print(*matrix[row])

    command = input()
