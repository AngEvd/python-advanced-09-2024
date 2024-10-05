from collections import deque

tools = deque(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))

while challenges:
    if not tools or not substances:
        break
    if tools[0] * substances[-1] in challenges:
        challenges.remove(tools[0] * substances[-1])
        tools.popleft()
        substances.pop()
    else:
        tools.append(tools.popleft() + 1)
        if substances[-1] - 1 > 0:
            substances[-1] -= 1
        else:
            substances.pop()

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print("Tools: " + ", ".join(map(str, [tool for tool in tools])))
if substances:
    print("Substances: " + ", ".join(map(str, [substance for substance in substances])))
if challenges:
    print("Challenges: " + ", ".join(map(str, [challenge for challenge in challenges])))
