class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


special_symbols = ("@", "*", "&", "%")
min_length = 8

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < min_length:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password.isdigit() or password.isalpha() or all(char in special_symbols for char in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(char in special_symbols for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
