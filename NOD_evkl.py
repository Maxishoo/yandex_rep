a = int(input())
b = int(input())
ma = max(a, b)
mi = min(a, b)

nok = ma
while 1:
    if nok % ma == 0 and nok % mi == 0:
        print(nok)
        break
    else:
        nok += 1
