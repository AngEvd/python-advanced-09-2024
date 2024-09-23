from collections import deque

kids = deque(input().split())
toss_number = int(input())

while len(kids) > 1:
    rotation = (toss_number - 1) % len(kids)
    kids.rotate(-rotation)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")