def d(a):
    delit = 2
    while delit * delit <= a:
        if a % delit == 0:
            return 0
        delit += 1
    if delit * delit == a:
        return 1
    return 1


a = int(input())
li = a
s = ''
for i in range(2, 10000):
    if i <= a and d(i) == 1:
        while a % i == 0:
            s += str(i) + ' * '
            a //= i
print(s[:-3], '=', li)
