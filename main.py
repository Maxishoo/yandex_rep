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