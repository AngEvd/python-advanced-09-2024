from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = [int(x) for x in input().split()]
wasted_water = 0

while cups_capacity and bottles_capacity:
    current_bottle = bottles_capacity.pop()
    current_cup = cups_capacity.popleft()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        cups_capacity.appendleft(current_cup)

if cups_capacity:
    print(f"Cups: " + " ".join(map(str, cups_capacity)))

if bottles_capacity:
    print(f"Bottles: " + " ".join(map(str, bottles_capacity)))

print(f"Wasted litters of water: {wasted_water}")
