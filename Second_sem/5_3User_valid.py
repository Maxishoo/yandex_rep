class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
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


def name_validation(name):
    if type(name) is not str:
        raise TypeError
    for i in name:
        if i.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя':
            raise CyrillicError

    if name != name.lower().capitalize():
        raise CapitalError

    return name


def user_validation(**kwargs):
    if "last_name" not in kwargs.keys() \
            or "first_name" not in kwargs.keys() \
            or "username" not in kwargs.keys() \
            or len(kwargs.keys()) != 3:
        raise KeyError
    for i in ["last_name", "first_name", "username"]:
        if type(kwargs[i]) is not str:
            raise TypeError
    kwargs['last_name'] = name_validation(kwargs['last_name'])
    kwargs['first_name'] = name_validation(kwargs['first_name'])
    kwargs['username'] = username_validation(kwargs['username'])
    return kwargs
