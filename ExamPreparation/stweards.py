from collections import deque

seats = input().split(", ")
sequence1 = deque(map(int, input().split(", ")))
sequence2 = deque(map(int, input().split(", ")))
rotations = 0
taken_seats = []

while rotations < 10 and len(taken_seats) < 3:
    number1 = sequence1.popleft()
    number2 = sequence2.pop()
    rotations += 1
    ascii_sum = chr(number1 + number2)
    if f"{number1}{ascii_sum}" in seats:
        if f"{number1}{ascii_sum}" not in taken_seats:
            taken_seats.append(f"{number1}{ascii_sum}")
    elif f"{number2}{ascii_sum}" in seats:
        if f"{number2}{ascii_sum}" not in taken_seats:
            taken_seats.append(f"{number2}{ascii_sum}")
    else:
        sequence1.append(number1)
        sequence2.appendleft(number2)

print(f"Seat matches: " + ", ".join(taken_seats))
print(f"Rotations count: {rotations}")
