from collections import deque

pumps_qty = int(input())

pumps = deque([int(x) for x in input().split()] for _ in range(pumps_qty))

pumps_copy = pumps.copy()
fuel_in_tank = 0
index = 0

while pumps_copy:
    pump = pumps_copy.popleft()

    refill, distance = pump
    fuel_in_tank += refill

    if fuel_in_tank >= distance:
        fuel_in_tank -= distance
    else:
        pumps.rotate(-1)
        pumps_copy = pumps.copy()
        fuel_in_tank = 0
        index += 1

print(index)