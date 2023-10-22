from itertools import product
def impl(a, b):
    return "(not a) or b"
def disunk(a, b):
    return a != b
def ecvival(a, b):
    return a == b

s = input().split()
d = {}
for i in s:
    if i.isupper():
        d[i] = 1
print(' '.join(sorted(d.keys())),'F')
while '~' not in s:
    print("cant ddooo")
