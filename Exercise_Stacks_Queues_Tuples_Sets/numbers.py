first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *numbers = input().split()
    command = first_command + " " + second_command

    if command == "Add First":
        [first_set.add(int(number)) for number in numbers]
    elif command == "Add Second":
        [second_set.add(int(number)) for number in numbers]
    elif command == "Remove First":
        [first_set.discard(int(number)) for number in numbers]
    elif command == "Remove Second":
        [second_set.discard(int(number)) for number in numbers]
    elif command == "Check Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
