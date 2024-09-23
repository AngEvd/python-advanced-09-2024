from collections import deque

working_bees = deque(map(int, input().split()))
nectar_line = deque(map(int, input().split()))
symbols = deque(input().split())

honey_made = 0

while working_bees and nectar_line:
    bee = working_bees.popleft()
    nectar = nectar_line.pop()
    if nectar < bee:
        working_bees.appendleft(bee)
        continue
    else:
        symbol = symbols.popleft()
        if symbol == "+":
            honey_made += abs(bee + nectar)
        elif symbol == "-":
            honey_made += abs(bee - nectar)
        elif symbol == "*":
            honey_made += abs(bee * nectar)
        elif symbol == "/" and nectar != 0:
            honey_made += abs(bee / nectar)
        else:
            continue

print(f"Total honey made: {honey_made}")

if working_bees:
    print(f"Bees left: " + ", ".join(map(str, working_bees)))

if nectar_line:
    print(f"Nectar left: " + ", ".join(map(str, nectar_line)))
