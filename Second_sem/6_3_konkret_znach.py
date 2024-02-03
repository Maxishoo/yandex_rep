from requests import get
from sys import stdin

adress = "http://" + input()
su = 0
for i in stdin:
    data = get(adress + i).json()
    for j in data:
        su += j
print(su)
