n = int(input())
a = dict()

for i in range(n):
    s = input().split()
    name = s[0][:-1]
    if name not in a:
        a[name] = []
    for j in range(1, len(s)):
        if j < len(s) - 1:
            a[name].append(s[j][:-1])
        else:
            a[name].append(s[j])
p = []
for key in a.keys():
    for j in a[key]:
        f = True
        for key2 in a.keys():
            if key2 != key:
                if j in a[key2]:
                    f = False
                    break
            if not f:
                break
        if f:
            p.append(j)
print('\n'.join(sorted(set(p))))
