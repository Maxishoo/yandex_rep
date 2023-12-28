n = int(input())
a = dict()
for i in range(n):
    s = input().split()
    for i in range(1, len(s)):
        if s[i] not in a:
            a[s[i]] = [s[0]]
        else:
            a[s[i]].append(s[0])
kasha = input()
if kasha not in a or len(a[kasha]) == 0:
    print('Таких нет')
else:
    a[kasha].sort()
    print('\n'.join(a[kasha]))