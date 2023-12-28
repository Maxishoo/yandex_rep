def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


a = input().split()
i = 0
while i < len(a):
    if a[i] == '-':
        a[i] = int(a[i - 2]) - int(a[i - 1])
        del a[i - 1]
        del a[i - 2]
        i -= 2
    elif a[i] == '+':
        a[i] = int(a[i - 2]) + int(a[i - 1])
        del a[i - 1]
        del a[i - 2]
        i -= 2
    elif a[i] == '*':
        a[i] = int(a[i - 2]) * int(a[i - 1])
        del a[i - 1]
        del a[i - 2]
        i -= 2
    elif a[i] == '/':
        a[i] = int(a[i - 2]) // int(a[i - 1])
        del a[i - 1]
        del a[i - 2]
        i -= 2
    elif a[i] == '!':
        a[i - 1] = factorial(int(a[i - 1]))
        del a[i]
        i -= 1
    elif a[i] == '#':
        a[i] = int(a[i - 1])
    elif a[i] == '~':
        a[i - 1] = -1 * int(a[i - 1])
        del a[i]
        i -= 1
    elif a[i] == '@':
        a[i - 3], a[i - 2], a[i - 1] = a[i - 2], a[i - 1], a[i - 3]
        del a[i]
        i -= 1
    i += 1
print(a[-1])
