s = input()
file = open(s, "r")
a = [int(i) for i in file.read().split()]
print(len(a))
kpol = 0
for i in a:
    if i >= 0:
        kpol += 1
print(kpol)
print(min(a))
print(max(a))
print(sum(a))
print(f"{sum(a) / len(a):.2f}")
