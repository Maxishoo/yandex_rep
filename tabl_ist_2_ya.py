from itertools import product

s = input().split()
d = {}
for i in s:
    if i.isupper():
        d[i] = 1
print(' '.join(sorted(d.keys())),'F')
s2 = ''
for i in range(len(s)):
    if s[i]=='->':
        s2+=' '+ "not("+s[i-1]+") or" + s[i+1]
mas = list(product([0, 1], repeat=len(d.keys())))
for i in mas:
    k = 0
    for j in sorted(d.keys()):
        d[j] = i[k]
        k += 1
    print(' '.join(str(i[n]) for n in range(len(i))), int(eval(s, {}, d)))
