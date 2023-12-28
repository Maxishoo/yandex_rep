def recursive_sum(*mas):
    if len(mas) == 0:
        return 0
    return mas[0] + recursive_sum(*mas[1:])


def recursive_digit_sum(number):
    if number == 0:
        return 0
    return number % 10 + recursive_digit_sum(number // 10)


def make_equation(*mas):
    if len(mas) == 1:
        return mas[0]
    return f"({make_equation(*mas[:-1])}) * x + {mas[-1]}"


def answer(f):
    def decorated(*args, **kargs):
        return f"Результат функции: {f(*args, **kargs)}"

    return decorated


def result_accumulator(f):
    cache = []

    def decorated(*args, method="accumulate"):
        cache.append(f(*args))
        if method == "drop":
            s = cache[:]
            cache.clear()
            return s

    return decorated


@result_accumulator
def a_plus_b(a, b):
    return a + b


def merge(arr1, arr2):
    arr3 = [None] * (len(arr1) + len(arr2))
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < len(arr1):
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1
    while j < len(arr2):
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
    return arr3


def merge_sort(args):
    if len(args) == 2:
        if args[1] < args[0]:
            args[0], args[1] = args[1], args[0]
        return args
    if len(args) == 1:
        return args
    return merge(merge_sort(args[:len(args) // 2]), merge_sort(args[len(args) // 2:]))


def same_type(f):
    def decorated(*args):
        tp = type(args[0])
        for i in args:
            if type(i) != tp:
                return False
        return f(*args)

    return decorated


@same_type
def a_plus_b(a, b):
    return a + b


from functools import lru_cache


def fibonacci(n):
    n1, n2 = 0, 1
    for i in range(n):
        yield n1
        n1, n2 = n2, n1 + n2


# print(*fibonacci(10), sep=', ')

# print(*(num**2 for num in range(5)))

def cycle(a):
    k = 0
    n = len(a)
    while 1:
        yield a[k]
        k += 1
        if k >= n:
            k = 0


# print(*cycle([1,2,3]))

# print(*(x for _, x in zip(range(44), cycle([1, 2, 3]))))


def make_linear(mass):
    if type(mass) != list:
        return [mass]
    if len(mass) == 1:
        return make_linear(mass[0])
    return make_linear(mass[0]) + make_linear(mass[1:])


print(make_linear([1, [2, [3, 4]], 5, 6]))
