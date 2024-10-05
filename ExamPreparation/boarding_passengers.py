from collections import deque


def boarding_passengers(capacity, *args):
    boarding_details = {}
    passengers = deque(args)
    groups = len(passengers)
    for _ in range(groups):
        passenger = passengers.popleft()
        if passenger[0] <= capacity:
            if passenger[1] not in boarding_details:
                boarding_details[passenger[1]] = 0
            capacity -= passenger[0]
            boarding_details[passenger[1]] += passenger[0]
        else:
            passengers.append(passenger)
        if capacity == 0:
            break

    sorted_details = sorted(boarding_details.items(), key=lambda kvp: (-kvp[1], kvp[0]))

    result = "Boarding details by benefit plan:"
    for detail in sorted_details:
        result += f"\n## {detail[0]}: {detail[1]} guests"
    if passengers and capacity == 0:
        result += "\nBoarding unsuccessful. Cruise ship at full capacity."
    else:
        if capacity > 0:
            result += f"\nPartial boarding completed. Available capacity: {capacity}."
        else:
            result += "\nAll passengers are successfully boarded!"

    return result


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print()
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print()
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))