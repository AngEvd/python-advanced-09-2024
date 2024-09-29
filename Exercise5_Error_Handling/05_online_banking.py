class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, balance, age = map(int, input().split(", "))

while True:
    command = input()
    if command == "End":
        break

    command_args = command.split("#")
    money = int(command_args[1])
    if command_args[0] == "Send Money":
        pin = int(command_args[2])
        if money > balance:
            raise MoneyNotEnoughError("MoneyNotEnoughError")
        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")
        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money

        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    else:
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        balance += money / 2
        print(f"{money / 2:.2f} money went straight into the bank account")
