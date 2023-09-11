n = int(input())
m = int(input())

t = int(input())
minute = (n * 60 + m + t) % (24 * 60)
print(f"{minute // 60:0>2}:{minute % 60:0>2}")
