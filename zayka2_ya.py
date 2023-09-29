n = int(input())
k = 0
for i in range(n):
    a = []
    s = input()
    while s != 'ВСЁ':
        a.append(s)
        s = input()
    if 'зайка' in a:
        k += 1
print(k)
