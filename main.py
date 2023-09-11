n = int(input())
m = int(input())

t = int(input())
print((n + t // 60) % 24)
print(f"{(n + t // 60) % 24:0>2}:{(m + t % 60) % 60:0>2}")
