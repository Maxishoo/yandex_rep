n = int(input())
a = []
for i in range(n):
    a.append(input())

for i in range(n):
    if a[i].count('зайка') == 0:
        print('Заек нет =(')
    else:
        print(a[i].find('зайка') + 1)