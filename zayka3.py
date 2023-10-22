s = input()
k = 0
while s != "Приехали!":
    if 'зайка' in s:
        k += 1
    s = input()
print(k)
