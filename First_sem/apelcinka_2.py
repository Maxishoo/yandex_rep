from itertools import *

n = int(input())
print('А Б В')
for i in product([i for i in range(1, n + 1)], repeat=3):
    if i[0] + i[1] + i[2] == n:
        print(f"{i[0]} {i[1]} {i[2]}")