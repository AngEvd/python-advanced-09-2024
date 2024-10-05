from collections import deque

monsters = deque(map(int, input().split(",")))
soldiers = list(map(int, input().split(",")))

kills = 0

while monsters and soldiers:
    monster = monsters.popleft()
    soldier = soldiers.pop()
    if soldier >= monster:
        kills += 1
        reduced_strike = soldier - monster
        if soldiers:
            soldiers[-1] += reduced_strike
        elif not soldiers and reduced_strike > 0:
            soldiers.append(reduced_strike)
    else:
        monsters.append(monster - soldier)

if not monsters:
    print("All monsters have been killed!")
if not soldiers:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {kills}")
