import math

n = float(input())
k = 1
a = []
x = 0
y = 0
nl = math.ceil(n / 2)
m = 1
for i in range(nl):
    aa = []
    for j in range(nl):
        aa.append(m)
        if m < i + 1:
            m += 1
    a.append(aa)
    m = 1

b = len(str(nl))
masstr = []
for i in range(nl):
    s = ''
    for j in range(nl):
        u = b * ' ' + str(a[i][j])
        s += u[-1 * b:]
        if j < n - 1:
            s += " "
    nll = int(n) // 2
    for j in range(1, nll + 1):
        u = b * ' ' + str(a[i][nll - j])
        s += u[-1 * b:]
        if j < n - 1:
            s += " "
    print(s)
    masstr.append(s)
for i in range(len(masstr) - 2, -1, -1):
    print(masstr[i])
