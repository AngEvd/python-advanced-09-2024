expression = list(input())

parentheses = []

for i in range(len(expression)):
    if expression[i] == "(":
        parentheses.append(i)
    elif expression[i] == ")":
        print("".join(expression[parentheses.pop():i + 1]))
