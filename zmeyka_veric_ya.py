n = int(input())
m = int(input())

k = 1
b = len(str(m * n))
a = [[0] * m for i in range(n)]
x = 0
y = 0
napr = 0
while k <= m * n:
    a[y][x] = k
    if napr == 0 and y + 1 < n:
        y += 1
    elif napr == 1 and y - 1 >= 0:
        y -= 1
    elif napr == 0:
        napr = 1
        x += 1
    elif napr == 1:
        napr = 0
        x += 1
    k += 1
for i in range(n):
    s = ''
    for j in range(m):
        u = b * ' ' + str(a[i][j])
        s += u[-1 * b:]
        if j < m - 1:
            s += " "
        k += 1
    print(s)
