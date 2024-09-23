from collections import deque

worms = list(map(int, input().split()))
holes = deque(map(int, input().split()))
matches = 0
worms_count = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
    else:
        worm -= 3
        if worm > 0:
            worms.append(worm)

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if matches < worms_count:
    if worms:
        print(f"Worms left: " + ", ".join(map(str, worms)))
    else:
        print("Worms left: none")
else:
    print("Every worm found a suitable hole!")

if holes:
    print(f"Holes left: " + ", ".join(map(str, holes)))
else:
    print("Holes left: none")


