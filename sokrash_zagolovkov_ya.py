ll = int(input())
n = int(input())
a = [input() for i in range(n)]

for i in range(len(a)):
    if len(a[i]) == 3:
        print(a[i])
        continue
    if len(a[i]) > ll:
        print(a[i][:ll - 3] + '...')
    else:
        print(a[i])
