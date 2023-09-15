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


nm = input()
pr = int(input())
wh = int(input())
mn = int(input())

st = str(wh) + "кг" + ' * ' + str(pr) + 'руб/кг'
print("================Чек================")
print(f'Товар:', f"{nm:>28}")
print(f'Цена:', f"{st:>29}")
print(f'Итого:', f"{str(wh*pr)+'руб':>28}")
print(f'Внесено:', f"{str(mn)+'руб':>26}")
print(f'Сдача:', f"{str(mn-wh*pr)+'руб':>28}")
print('===================================')


n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

y = (n * k1 - n * m) // (k1 - k2)
x = n - y
print(x, y)


###################################################
a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c
if a == 0:
    if b == 0 and c == 0:
        print("Infinite solutions")
    elif b == 0 and c != 0:
        print("No solution")
    elif b != 0:
        x = -1 * c / b
else:
    if d < 0:
        print("No solution")
    elif d == 0:
        print(f"{(-1 * b) / (2 * a):.2f}")
    elif d > 0:
        x1 = (-1 * b + d ** 0.5) / (2 * a)
        x2 = (-1 * b - d ** 0.5) / (2 * a)
        print(f"{min(x1, x2):.2f}", f"{max(x1, x2):.2f}")
