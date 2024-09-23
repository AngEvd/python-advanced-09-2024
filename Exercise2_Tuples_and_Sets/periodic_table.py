elements_count = int(input())

periodic_table = set()

for _ in range(elements_count):
    for element in input().split():
        periodic_table.add(element)

print(*periodic_table, sep="\n")