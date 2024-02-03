import math

x = float(input())
l1 = math.log(math.pow(x, (3 / 16)), 32)
l2 = math.pow(x, math.cos((math.pi * x) / (2 * math.e)))
l3 = math.pow(math.sin(x / math.pi), 2)
print(l1 + l2 - l3)
