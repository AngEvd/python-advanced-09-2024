guests = int(input())

reservations = set()

for _ in range(guests):
    reservations.add(input())

guest = input()

while guest != "END":
    reservations.discard(guest)
    guest = input()

print(len(reservations))
print(*sorted(reservations), sep="\n")
