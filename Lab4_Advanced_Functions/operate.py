from functools import reduce


def operate(operator, *args):

    def add():
        return sum(args)

    def subtract():
        return reduce(lambda x, y: x - y, args)

    def multiply():
        return reduce(lambda x, y: x * y, args)

    def divide():
        return reduce(lambda x, y: x / y if y != 0 else x, args)

    mapper = {"+": add,
              "-": subtract,
              "/": divide,
              "*": multiply
              }

    return mapper[operator]()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 3, 0, 5))
