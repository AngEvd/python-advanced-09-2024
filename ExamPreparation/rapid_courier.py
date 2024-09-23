from collections import deque

packages = list(map(int, input().split()))
couriers = deque(map(int, input().split()))

total_weight = 0

while packages and couriers:
    package = packages.pop()
    courier = couriers.popleft()
    if courier >= package:
        courier -= 2 * package
        if courier > 0:
            couriers.append(courier)
        total_weight += package
    else:
        total_weight += courier
        packages.append(package - courier)

print(f"Total weight: {total_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to"
          f" deliver the following packages: {', '.join(map(str, packages))}")
elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")
