s = []
with open("1.txt", 'r', encoding="utf-8") as file:
    for line in file:
        s.append(line.rstrip("\n"))
for st in s:
    res = ""
    for i in st:
        if ord(i) < 128:
            res += i
        else:
            b = bin(ord(i))[2:]
            b = b[len(b) - 8:len(b)]
            res = res + chr(int(b, 2))
    print(res)
