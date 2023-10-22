a = int(input())
k = 1
konline = 1
sp = []
fl = 1
while k <= a:
    sl = []
    for i in range(konline):
        sl.append(k)
        if k == a:
            fl = 0
            break
        k += 1
    sp.append(sl)
    konline += 1
    if fl == 0:
        break
# print(sp)
s = ''
for i in sp[len(sp) - 1]:
    s += str(i) + ' '
b = len(s[:-1])
for i in range(len(sp)):
    st = ''
    for j in range(len(sp[i])):
        st += str(sp[i][j]) + ' '
    print(f"{st[:-1]:^{b}}")
