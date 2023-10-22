n = int(input())
fl = 1
hn = [0]
nn = [int(input()) for i in range(n)]
for i in range(n):
    bn = nn[i]
    nwhn = []
    for rn in range(0, 256):
        tmpr = rn * 256
        for mn in range(0, 256):
            tmp = tmpr + mn * 256 * 256
            if (tmp > bn):
                break
            for h in hn:
                hnew = (37 * (mn + rn + h)) % 256
                if hnew < 100 and bn == hnew + tmp:
                    nwhn.append(hnew)
    if len(nwhn) == 0:
        print(i)
        fl = 0
        break
    hn = nwhn
if fl == 1:
    print(-1)
