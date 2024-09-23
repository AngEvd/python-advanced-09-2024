parentheses = input()

stack = []
balanced = True

for char in parentheses:
    if char in ")]}" and not stack:
        balanced = False
        break

    elif char in "{[(":
        stack.append(char)

    else:
        if stack.pop() + char not in ["()", "[]", "{}"]:
            balanced = False
            break

print("YES" if balanced else "NO")
