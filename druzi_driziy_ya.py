s = input()
a = dict()
while s != '':
    druzi = s.split()
    if druzi[0] not in a:
        a[druzi[0]] = [druzi[1]]
    else:
        a[druzi[0]].append(druzi[1])
    if druzi[1] not in a:
        a[druzi[1]] = [druzi[0]]
    else:
        a[druzi[1]].append(druzi[0])
    s = input()
people = sorted(a.keys())
for i in people:
    druz2 = []
    for j in a[i]:
        for z in a[j]:
            if z != i and z not in a[i]:
                druz2.append(z)
    st = ', '.join(sorted(set(druz2)))
    print(f"{i}: {st}")