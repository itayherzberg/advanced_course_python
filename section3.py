import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, character):
        self._username = username
        self._character = character  # the character that risen the exception

    def __str__(self):
        return "The username contains an illegal character \"{}\" at index {}"\
            .format(self._character, self._username.index(self._character))


class UsernameTooShort(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercaseCharacter(PasswordMissingCharacter):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercaseCharacter(PasswordMissingCharacter):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigitCharacter(PasswordMissingCharacter):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecialCharacter(PasswordMissingCharacter):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The password is too long"


def check_username(username):
    # check if all the characters in the username are valid
    for x in username:
        if not (x.isalpha() or x.isdigit() or (isinstance(x, str) and x == '_')):
            raise UsernameContainsIllegalCharacter(username, x)

    # check the length of the username
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()

    return True


def check_password(password):
    # check the length of the password
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()

    # declare counters for each input type
    lower_letter_c = 0
    upper_letter_c = 0
    number_c = 0
    special_characters = 0

    # check if all the characters in the password are valid
    for x in password:
        if x.isalpha() and x.islower():
            lower_letter_c += 1
        elif x.isalpha() and x.isupper():
            upper_letter_c += 1
        elif x.isdigit():
            number_c += 1
        elif x in string.punctuation:
            special_characters += 1

    if upper_letter_c == 0:
        raise PasswordMissingUppercaseCharacter()
    if lower_letter_c == 0:
        raise PasswordMissingLowercaseCharacter()
    if number_c == 0:
        raise PasswordMissingDigitCharacter()
    if special_characters == 0:
        raise PasswordMissingSpecialCharacter()

    return True


def check_input(username, password):
    if check_username(username) and check_password(password):
        print("OK")


def main():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    is_valid = False  # indicates if the input is valid

    while not is_valid:
        try:
            check_input(username, password)
            is_valid = True
        except UsernameContainsIllegalCharacter as e:
            print(e)
        except UsernameTooShort as e:
            print(e)
        except UsernameTooLong as e:
            print(e)
        except PasswordMissingCharacter as e:
            print(e)
        except PasswordTooShort as e:
            print(e)
        except PasswordTooLong as e:
            print(e)
        finally:
            if not is_valid:
                username = input("Enter a username: ")
                password = input("Enter a password: ")


if __name__ == "__main__":
    main()
