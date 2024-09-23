numbers = tuple(float(x) for x in input().split())

occurrences = {}

for number in numbers:
    occurrences[number] = numbers.count(number)

for name, occurrence in occurrences.items():
    print(f"{name} - {occurrence} times")
