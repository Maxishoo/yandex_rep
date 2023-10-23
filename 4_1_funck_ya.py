def print_hello(name):
    print(f"Hello, {name}!")


def gcd(a, b):
    ma = max(a, b)
    mi = min(a, b)
    if ma % mi == 0:
        return mi
    else:
        while mi != 0:
            ost1 = ma % mi
            if ost1 == 0:
                return mi
            ost2 = mi % ost1
            ma = ost1
            mi = ost2
        return ma


def number_length(a):
    return len(str(a))


def month(n, lg):
    d1 = "Январь Февраль Март Апрель Май Июнь Июль Август Сентябрь Октябрь Ноябрь Декабрь"
    d2 = "January February March April May June July August September October November December"
    d1, d2 = d1.split(), d2.split()
    if lg == "en":
        return d2[n - 1]
    else:
        return d1[n - 1]


def split_numbers(s):
    return tuple(s.split())


def modern_print(s):
    if s not in history:
        print(s)
        history.append(s)


history = []


def can_eat(a, b):
    if (abs(b[0] - a[0]) == 2 and abs(b[1] - a[1]) == 1) \
            or (abs(b[0] - a[0]) == 1 and abs(b[1] - a[1]) == 2):
        return True
    else:
        return False


def is_palindrome(n):
    if type(n) is int:
        if str(n) == str(n)[::-1]:
            return True
    else:
        if n == n[::-1]:
            return True
    return False


def is_prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


print(is_palindrome([0, 0]))


def merge(a, b):
    m = list(a + b)
    res = []
    while len(m) != 0:
        res.append(min(m))
        m.remove(min(m))
    return tuple(res)


print(merge((7, 12), (1, 9, 50)))
