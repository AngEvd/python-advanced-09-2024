from collections import deque

food_qty = int(input())

food_orders = deque(map(int, input().split()))

print(max(food_orders))

for order in list(food_orders):
    if order <= food_qty:
        food_qty -= order
        food_orders.popleft()
    else:
        break

if food_orders:
    print(f"Orders left: " + " ".join(map(str, food_orders)))

else:
    print("Orders complete")
