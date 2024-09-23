rows, columns = map(int, input().split())

snake = input()

snake_index = 0
matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(columns):
        matrix[row].append(snake[snake_index % len(snake)])
        snake_index += 1
    if row % 2 != 0:
        matrix[row].reverse()

for row in range(rows):
    print(*matrix[row], sep="")
