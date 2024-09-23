from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(y) for y in input().split()])
intelligence_value = int(input())
bullets_in_barrel = barrel_size
money_spend = 0

while bullets and locks:
    bullet = bullets.pop()
    bullets_in_barrel -= 1
    money_spend += bullet_price

    if bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if bullets_in_barrel == 0:
        if bullets:
            print("Reloading!")
            bullets_in_barrel += barrel_size


if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - money_spend}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
