import json

s1 = input()
s2 = input()
with open(s1, 'r', encoding="UTF-8") as fusers:
    users = json.load(fusers)
with open(s2, 'r', encoding="UTF-8") as fupdates:
    updates = json.load(fupdates)
newdata = {}
for i in users:
    for j in updates:
        if i['name'] == j['name']:
            for key in j.keys():
                if key != "name":
                    if key not in i.keys() or i[key] < j[key]:
                        i[key] = j[key]
for us in users:
    nm = us['name']
    del us['name']
    newdata[nm] = us

with open(s1, 'w', encoding="UTF-8") as file:
    json.dump(newdata, file, ensure_ascii=False, indent=2)