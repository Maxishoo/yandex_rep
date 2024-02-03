from requests import get

adress = "http://" + input()
data = get(adress).json()
s = 0
for i in data:
    if type(i) is int or type(i) is float:
        s += i
print(i)
