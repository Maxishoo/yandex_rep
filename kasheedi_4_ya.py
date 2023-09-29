n = int(input())
d = dict()
for i in range(n):
    s = input().split()
    key = s[1]
    chel = s[0]
    if key not in d:
        d[key] = [chel]
    else:
        d[key].append(chel)
nkey = input()
if len(d[nkey])==0:
    print("Таких нет")
else:
    print('\n'.join(d[key]))