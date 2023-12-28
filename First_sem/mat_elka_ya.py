k = int(input())
b = 1
ln = 1
s = ''
ch = 0
for j in range(1, k + 1):
    if ch == ln:
        print(s[:len(s) - 1])
        s = ''
        ln += 1
        ch = 0
    s += str(j) + ' '
    ch += 1
print(s)
