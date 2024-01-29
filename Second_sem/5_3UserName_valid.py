class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    if type(name) is not str:
        raise TypeError
    for i in name:
        if i.lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789_':
            raise BadCharacterError
    if name[0] in "0123456789":
        raise StartsWithDigitError
    return name
