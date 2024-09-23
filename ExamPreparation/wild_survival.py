from collections import deque

bee_swarm = deque(map(int, input().split()))
bee_eaters = list(map(int, input().split()))

while bee_swarm and bee_eaters:
    bees = bee_swarm.popleft()
    bee_eater = bee_eaters.pop()
    while bees and bee_eater:
        if bees >= 7:
            bee_eater -= 1
            bees -= 7
        else:
            bees = 0
    if bees:
        bee_swarm.append(bees)
    if bee_eater:
        bee_eaters.append(bee_eater)

print("The final battle is over!")
if not bee_swarm and not bee_eaters:
    print("But no one made it out alive!")
elif bee_swarm:
    print(f"Bee groups left: {', '.join(map(str, bee_swarm))}")
else:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")

