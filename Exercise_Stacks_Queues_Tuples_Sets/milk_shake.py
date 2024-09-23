from collections import deque

milk_shakes = 0

chocolates = deque(map(int, input().split(", ")))
milk_cups = deque(map(int, input().split(", ")))

while chocolates and milk_cups and milk_shakes < 5:
    chocolate = chocolates.pop()
    milk_cup = milk_cups.popleft()
    if chocolate <= 0 and milk_cup <= 0:
        continue
    elif chocolate <= 0:
        milk_cups.appendleft(milk_cup)
        continue
    elif milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milk_shakes += 1
    else:
        milk_cups.append(milk_cup)
        chocolates.append(chocolate - 5)

if milk_shakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

if chocolates:
    print("Chocolate: " + ", ".join(map(str, chocolates)))
else:
    print("Chocolate: empty")

if milk_cups:
    print("Milk: " + ", ".join(map(str, milk_cups)))
else:
    print("Milk: empty")
