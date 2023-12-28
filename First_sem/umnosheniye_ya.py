n = int(input())
ln = int(input())
sp = []
a = []
for i in range(n):
    a.append(i + 1)
for i in range(1, n + 1):
    sp.append(a)
    a.append(i + 1)
    a = [i + 1]
    for j in range(1, n):
        a.append(a[0] * sp[0][j])
##beautifull vivod
for i in range(n):
    s = ''
    for j in range(n):
        ls = len(str(sp[i][j]))
        u = ((ln - ls) // 2) * ' ' + str(sp[i][j])
        s += u + (ln - len(u)) * ' '
        if j < n - 1:
            s += "|"
    print(s)
    if i < n - 1:
        print('-' * len(s))
