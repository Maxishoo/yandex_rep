def merge(a, b):
    try:
        a_it = iter(a)
        b_it = iter(b)
    except TypeError:
        raise StopIteration

    typp = type(a[0])
    for i in a:
        if type(i) is not typp:
            raise TypeError
    for i in b:
        if type(i) is not typp:
            raise TypeError
    typp = type(b[0])
    for i in b:
        if type(i) is not typp:
            raise TypeError
    for i in a:
        if type(i) is not typp:
            raise TypeError

    if list(a) != sorted(a) or list(b) != sorted(b):
        raise ValueError
    return tuple(sorted(list(a) + list(b)))


print(merge((1,), ["a", 1]))
