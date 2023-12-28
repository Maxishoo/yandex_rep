def d(a):
    delit = 2
    while delit * delit < a:
        if a % delit == 0:
            return 'NO'
        delit += 1
    if delit * delit == a:
        return 'NO'
    return 'YES'


a = int(input())
if a == 0 or a == 1:
    print('NO')
else:
    print(d(a))
