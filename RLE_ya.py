s = input()
k = 0
save = s[0]
i = 0
while i < len(s):
    if s[i] == save:
        k += 1
        i += 1
    else:
        print(save, k)
        save = s[i]
        k = 0
print(save, k)
