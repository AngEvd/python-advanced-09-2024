from collections import deque

total_caffeine = 0

milligrams = list(map(int, input().split(", ")))
drinks = deque(map(int, input().split(", ")))

while milligrams and drinks:
    if milligrams[-1] * drinks[0] <= 300 - total_caffeine:
        total_caffeine += milligrams.pop() * drinks.popleft()
    else:
        milligrams.pop()
        drinks.append(drinks.popleft())
        total_caffeine = max(0, total_caffeine - 30)

    if total_caffeine >= 300:
        break

if drinks:
    print(f"Drinks left: " + ", ".join(map(str, drinks)))
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
