odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    name_ascii_sum = sum(value for value in [ord(char) for char in input()]) // row
    if name_ascii_sum % 2 == 0:
        even_set.add(name_ascii_sum)
    else:
        odd_set.add(name_ascii_sum)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.union(even_set), sep=", ")
