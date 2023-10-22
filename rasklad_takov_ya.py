from itertools import *

sp = "10 2 3 4 5 6 7 8 9 валет дама король туз".split()
sp2 = "бубен пик треф червей".split()
a = [[i, j] for i, j in list(product(sp, sp2))]
mast = input()
card = input()
if mast == "буби":
    mast = 'бубен'
if mast == "пики":
    mast = 'пик'
if mast == "трефы":
    mast = 'треф'
if mast == "черви":
    mast = 'червей'
k = 0
for i in list(combinations(a, 3)):
    vb = list(i)
    teckmasts = [vb[0][1], vb[1][1], vb[2][1]]
    teckcards = [vb[0][0], vb[1][0], vb[2][0]]
    if mast in teckmasts and card not in teckcards:
        print(', '.join([p[0] + " " + p[1] for p in vb]))
        k += 1
    if k == 10:
        break
