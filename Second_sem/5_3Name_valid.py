class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if type(name) is not str:
        raise TypeError
    for i in name:
        if i.lower() not in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя':
            raise CyrillicError

    if name != name.lower().capitalize():
        raise CapitalError

    return name


print(name_validation("ИFов"))
