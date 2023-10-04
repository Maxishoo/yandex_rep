n = int(input())
a = dict()
for i in range(n):
    s = input().split()
    if f"{s[0][:-1]} {s[1][:-1]}" not in a:
        a[f"{s[0][:-1]} {s[1][:-1]}"] = 1
    else:
        a[f"{s[0][:-1]} {s[1][:-1]}"] += 1
maxk = 0
for key, val in a.items():
    maxk = max(maxk, val)
print(maxk)
