stack = []

lines_number = int(input())

for _ in range(lines_number):
    user_line = input()

    if user_line.startswith("1"):
        command, number = user_line.split()
        stack.append(int(number))

    elif user_line == "2" and stack:
        stack.pop()

    elif user_line == "3" and stack:
        print(max(stack))

    elif user_line == "4" and stack:
        print(min(stack))

print(", ".join(map(str, reversed(stack))))
