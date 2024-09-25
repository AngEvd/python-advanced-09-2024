from functools import reduce


def subtract(*args):
    return reduce(lambda x, y: x - y, args)

print(subtract(1, 2, 3))

