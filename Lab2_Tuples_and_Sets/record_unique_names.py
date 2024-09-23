number = int(input())
names = set()

for _ in range(number):
    names.add(input())

print(*names, sep="\n")
