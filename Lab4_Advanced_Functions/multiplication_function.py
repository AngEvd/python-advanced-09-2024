def multiply(*args):
    result = 1
    if args:
        for num in args:
            result *= num
    else:
        result = 0
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
