from itertools import *

a = [0, 1]
s = input()
print("a b c f")
for i in list(product(a, a, a)):
    a, b, c = i[0], i[1], i[2]
    print(a, b, c, int(eval(s)))
