players = input().split(", ")

matrix = []
turn = 0
skip_turn = {players[0]: False, players[1]: False}

for _ in range(6):
    matrix.append(input().split())

while True:
    turn += 1
    current_player = players[0] if turn % 2 != 0 else players[1]
    coordinates = list(int(x) for x in input() if x.isdigit())
    next_cell = matrix[coordinates[0]][coordinates[1]]
    if skip_turn[current_player]:
        skip_turn[current_player] = False
        continue
    if next_cell == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    if next_cell == "T":
        players.remove(current_player)
        print(f"{current_player} is out of the game! The winner is {players[0]}.")
        break
    if next_cell == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        skip_turn[current_player] = True


