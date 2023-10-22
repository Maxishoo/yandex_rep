def countchifr(a):
    kch, knch = 0, 0
    while a > 0:
        b = a % 10
        if b % 2 == 0:
            kch += 1
        else:
            knch += 1
        a //= 10
    return (kch, knch)


fr = open(input(), 'r', encoding='UTF-8')
f1 = open(input(), 'w', encoding='UTF-8')
f2 = open(input(), 'w', encoding='UTF-8')
f3 = open(input(), 'w', encoding='UTF-8')
num = []
for line in fr:
    num.append([int(i) for i in line.split()])
for i in range(len(num)):
    s1, s2, s3 = [], [], []
    for j in range(len(num[i])):
        m = countchifr(num[i][j])
        if m[0] > m[1]:
            s1.append(num[i][j])
        elif m[1] > m[0]:
            s2.append(num[i][j])
        else:
            s3.append(num[i][j])
    if len(s1) != 0:
        f1.write(' '.join([str(v) for v in s1]))
    f1.write('\n')
    if len(s2) != 0:
        f2.write(' '.join([str(v) for v in s2]))
    f2.write('\n')
    if len(s3) != 0:
        f3.write(' '.join([str(v) for v in s3]))
    f3.write('\n')
fr.close()
f1.close()
f2.close()