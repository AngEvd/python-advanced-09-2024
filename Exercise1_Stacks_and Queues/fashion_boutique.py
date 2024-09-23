clothes = list(map(int, input().split()))

rack_capacity = int(input())

rack = []

racks_count = 1

while clothes:
    if clothes[-1] <= rack_capacity - sum(rack):
        rack.append(clothes.pop())
    else:
        racks_count += 1
        rack = []

print(racks_count)