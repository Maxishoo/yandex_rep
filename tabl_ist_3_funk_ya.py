from itertools import product


def findpos2(s):
    kol = 0
    for i in range(len(s)):
        if s[i] == "(":
            kol += 1
        if s[i] == ")":
            if kol == 0:
                return i
            kol -= 1


def calcs(s):
    pos = s.find("~")
    if pos != -1:
        s = "(" + s.replace("~", ")==(") + ")"
        s = f(s)
    pos = s.find("^")
    if pos != -1:
        s = "(" + s.replace("^", ")!=(") + ")"
        s = f(s)
    pos = s.find("->")
    if pos != -1:
        s = "(" + s.replace("->", ")<=(") + ")"
        s = f(s)
    zn = eval(s)
    if zn:
        return "1"
    else:
        return "0"


def f(s):
    while 1:
        if len(s) == 1:
            break
        pos = s.find("(")
        if pos != -1:
            pos2 = pos + 1 + findpos2(s[pos + 1:])
            s = s[:pos] + f(s[pos + 1:pos2]) + s[pos2 + 1:]
        else:
            return calcs(s)
    return s


s = input()
ss = s
d = {}
for i in s:
    if i.isupper():
        d[i] = 1
print(' '.join(sorted(d.keys())), 'F')
mas = list(product([0, 1], repeat=len(d.keys())))
for i in mas:
    k = 0
    for j in sorted(d.keys()):
        s = s.replace(j, str(i[k]))
        k += 1
    print(' '.join(str(h) for h in i), f(s))
    s = ss
