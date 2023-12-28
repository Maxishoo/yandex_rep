a = input()
x = 0
y = 0
while a != "СТОП":
    c = int(input())
    if a == "СЕВЕР":
        y += c
    elif a == "ВОСТОК":
        x += c
    elif a == "ЮГ":
        y -= c
    elif a == "ЗАПАД":
        x -= c
    a = input()
print(y)
print(x)
