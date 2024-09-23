rows, columns = map(int, input().split(" "))

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(columns):
        matrix[row].append(f"{chr(row + 97)}{chr(col + row + 97)}{chr(row + 97)}")

for row in range(rows):
    print(*matrix[row])
