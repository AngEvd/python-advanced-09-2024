cars_count = int(input())

cars = set()

for _ in range(cars_count):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)
    else:
        cars.remove(car_number)

if cars:
    print(*cars, sep="\n")
else:
    print("Parking Lot is Empty")
