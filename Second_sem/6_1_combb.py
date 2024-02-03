import math

x, y = map(float, input().split())
p, f = map(float, input().split())

x2, y2 = p * math.cos(f), p * math.sin(f)
print(math.dist((x, y), (x2, y2)))
