n = int(input())
m = int(input())
k = 0
a = []
for i in range(n + m):
    a.append(input())
ll = []
for i in a:
    if a.count(i) == 1:
        ll.append(i)
if len(ll) == 0:
    print("Таких нет")
else:
    print('\n'.join(sorted(ll)))
