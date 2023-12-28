n = int(input())
products = []
for i in range(n):
    products.append(input())
recepty = int(input())
moshemgot = []
for i in range(recepty):
    f = True
    name = input()
    nn = int(input())
    for j in range(nn):
        if input() not in products:
            f = False
    if f:
        moshemgot.append(name)
if len(moshemgot) != 0:
    moshemgot.sort()
    print('\n'.join(moshemgot))
else:
    print('Готовить нечего')
