with open("numbers.num", "rb") as f:
    a = f.read()
su = 0
for i in range(0, len(a), 2):
    su += int.from_bytes(a[i:i + 2], "big")
print(su % 2 ** 16)
print(1)