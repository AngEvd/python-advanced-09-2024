from collections import deque

water_available = int(input())

people = deque()

name = input()

while name != "Start":
    people.append(name)
    name = input()

user_line = input()

while user_line != "End":
    if user_line.isdigit():
        person_name = people.popleft()
        water_wanted = int(user_line)
        if water_available >= water_wanted:
            water_available -= water_wanted
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    else:
        command, liters = user_line.split()
        water_available += int(liters)
    user_line = input()

print(f"{water_available} liters left")
