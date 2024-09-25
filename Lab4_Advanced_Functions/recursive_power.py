def recursive_power(number, power):
    if power == 0:
        result = 1
    elif power == 1:
        result = number
    else:
        result = number * recursive_power(number, power - 1)
    return result


print(recursive_power(2, 8))