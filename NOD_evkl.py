def nodd(a, b):
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


n = int(input())
if n == 0:
    print(0)
else:
    nodik = int(input())
    for i in range(n - 1):
        a = int(input())
        nodik = nodd(nodik, a)
    print(nodik)
