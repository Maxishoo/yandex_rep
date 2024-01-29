import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8,
                        possible_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                        at_least_one=str.isdigit):
    if type(password) is not str:
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    for i in password:
        if i not in possible_chars:
            raise PossibleCharError
    for i in password:
        if at_least_one(i):
            break
    else:
        raise NeedCharError
    return hashlib.sha256(password.encode()).hexdigest()


print(password_validation("Hello12345"))
