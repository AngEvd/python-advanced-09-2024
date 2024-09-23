from collections import deque

contestants = deque(map(int, input().split()))
pies = list(map(int, input().split()))

while contestants and pies:
    contestant = contestants.popleft()
    pie = pies.pop()
    if contestant >= pie:
        contestant -= pie
        if contestant > 0:
            contestants.append(contestant)
    else:
        pie -= contestant
        if pie > 1:
            pies.append(pie)
        else:
            if pies:
                pies[-1] += pie
            else:
                pies.append(pie)

if contestants and not pies:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants))}")

elif pies and not contestants:
    print(f"Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies))}")

else:
    print("We have a champion!")
