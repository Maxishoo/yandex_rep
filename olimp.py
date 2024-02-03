n = int(input())
d = dict()
for i in range(n):
    st = input().split()
    if st[0] == "+":
        if st[2] in d.keys():
            d[st[2]] += int(st[1])
        else:
            d[st[2]] = int(st[1])
    else:
        max_k = 0
        max_word = None
        for j in d.keys():
            if d[j] > max_k or (d[j] == max_k and (max_word == None or j < max_word)):
                print(1)