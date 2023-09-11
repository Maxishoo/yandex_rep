a = int(input())
b = int(input())

mi = min(a, b)
ma = max(a, b)
c = 0
i = 0
while ma > 0:
    if mi > 0:
        c += (ma % 10 + mi % 10) % 10 * 10 ** i
        mi = mi // 10
    else:
        c += ma % 10 * 10 ** i
    ma = ma // 10
    i += 1
print(c)


n = int(input())
m = int(input())

t = int(input())
minute = (n * 60 + m + t) % (24 * 60)
print(f"{minute // 60:0>2}:{minute % 60:0>2}")



a = int(input())
b = int(input())
c = int(input())
d=(abs(a-b)/c)
print(f"{d:.{2}f}")