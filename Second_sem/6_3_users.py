from requests import get

address = "http://" + input() + "/users"
data = get(address).json()
users = []
for d in data:
    users.append([d["last name"], d["first name"]])
for i in sorted(users):
    print(i[0], i[1])
