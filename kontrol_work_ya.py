n = int(input())
minsr = None
for i in range(n):
    sp = []
    s = input()
    while s != "next":
        sp.append(int(s))
        s = input()
    if minsr is None:
        minsr = sum(sp) / len(sp)
    else:
        minsr = max(minsr, sum(sp) / len(sp))
print(f"{minsr:.2f}")
