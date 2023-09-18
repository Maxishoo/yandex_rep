c = int(input())
d = int(input())
nod = 1
a = max(c,d)
b = min(c,d)

while b!=0:
    #a, b = b, a % b
    c = a
    a = b
    b = c % b
print(a)