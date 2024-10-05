from collections import deque

times = deque(map(int, input().split()))
tasks = list(map(int, input().split()))

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while tasks and times:
    time = times.popleft()
    task = tasks.pop()
    result = time * task
    if 0 <= result <= 60:
        ducks["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        ducks["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        tasks.append(task - 2)
        times.append(time)


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in ducks.items():
    print(f"{key}: {value}")
