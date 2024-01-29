class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (int, float):
        raise TypeError
    d = b ** 2 - 4 * a * c
    if a == 0:
        if b == 0 and c == 0:
            raise InfiniteSolutionsError
        elif b == 0 and c != 0:
            raise NoSolutionsError
        elif b != 0:
            return (-1 * c / b, -1 * c / b)
    else:
        if d < 0:
            raise NoSolutionsError
        elif d == 0:
            return ((-1 * b) / (2 * a), (-1 * b) / (2 * a))
        elif d > 0:
            x1 = (-1 * b + d ** 0.5) / (2 * a)
            x2 = (-1 * b - d ** 0.5) / (2 * a)
            return (min(x1, x2), max(x1, x2))


print(find_roots(0, 2, 1))
