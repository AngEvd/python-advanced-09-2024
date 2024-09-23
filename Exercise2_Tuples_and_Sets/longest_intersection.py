lines_number = int(input())

longest_intersection = []

for _ in range(lines_number):
    first_range, second_range = [index.split(",") for index in input().split("-")]

    first_set = set(range(int(first_range[0]), int(first_range[1]) + 1))
    second_set = set(range(int(second_range[0]), int(second_range[1]) + 1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
