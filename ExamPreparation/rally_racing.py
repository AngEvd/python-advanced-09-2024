size = int(input())
racing_number = input()

racing_route = []
car_position = [0, 0]
distance = 0

for _ in range(size):
    racing_route.append(input().split())


def find_tunel_end(matrix: list) -> tuple:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "T":
                return row, col


moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        racing_route[car_position[0]][car_position[1]] = "C"
        break
    row_move, col_move = moves[command]
    next_row = car_position[0] + row_move
    next_col = car_position[1] + col_move
    next_cell = racing_route[next_row][next_col]
    if next_cell == ".":
        distance += 10
        car_position = [next_row, next_col]
    elif next_cell == "T":
        distance += 30
        racing_route[next_row][next_col] = "."
        car_position[0], car_position[1] = find_tunel_end(racing_route)
        racing_route[car_position[0]][car_position[1]] = "."
    elif next_cell == "F":
        distance += 10
        racing_route[next_row][next_col] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        break

print(f"Distance covered {distance} km.")
[print(*row, sep="") for row in racing_route]
