from collections import deque

initial_fuel = list(map(int, input().split()))
consumption_index = deque(map(int, input().split()))
fuel_needed = deque(map(int, input().split()))
reached_altitudes = []
altitude = 0
fail = False

while initial_fuel:
    fuel = initial_fuel.pop()
    consumption = consumption_index.popleft()
    need = fuel_needed.popleft()
    altitude += 1
    if fuel - consumption < need:
        fail = True
        print(f"John did not reach: Altitude {altitude}")
        break
    else:
        print(f"John has reached: Altitude {altitude}")
        reached_altitudes.append(altitude)

if fail:
    print(f"John failed to reach the top.")
    if reached_altitudes:
        print(f"Reached altitudes: " + ", ".join([f"Altitude {alt}" for alt in reached_altitudes]))
    else:
        print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")
