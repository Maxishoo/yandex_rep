import math
from sys import stdin

a = []
for st in stdin:
    a.append(list(map(int, st.split())))
for i in a:
    print(math.gcd(*i))
