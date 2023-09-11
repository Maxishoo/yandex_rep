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
