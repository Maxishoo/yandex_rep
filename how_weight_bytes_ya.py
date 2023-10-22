import os

size = os.path.getsize(input())
if size < 1:
    print(f"{int(size * 8) + 1}б")
elif size < 1024 - 1:
    print(f"{size}Б")
elif size < 1024 * 1024 - 1:
    print(f"{int(size / 1024) + 1}КБ")
elif size < 1024 * 1024 * 1024 - 1:
    print(f"{int(size / 1024 ** 2) + 1}КБ")
else:
    print(f"{int(size / 1024 ** 3) + 1}ГБ")