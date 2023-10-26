def make_list(lengh, val=0):
    return [val for i in range(lengh)]


def make_matrix(size, val=0):
    if type(size) == int:
        return [[val for i in range(size)] for j in range(size)]
    else:
        return [[val for i in range(size[0])] for j in range(size[1])]


def nodd(a, b):
    ma = max(a, b)
    mi = min(a, b)
    if ma % mi == 0:
        return mi
    else:
        while mi != 0:
            ost1 = ma % mi
            if ost1 == 0:
                return mi
            ost2 = mi % ost1
            ma = ost1
            mi = ost2
        return ma


def gcd(num):
    res = num[0]
    for i in range(1, len(num)):
        res = nodd(res, num[i])
    return res


def month(n, lg='ru'):
    d1 = "Январь Февраль Март Апрель Май Июнь Июль Август Сентябрь Октябрь Ноябрь Декабрь"
    d2 = "January February March April May June July August September October November December"
    d1, d2 = d1.split(), d2.split()
    if lg == "en":
        return d2[n - 1]
    else:
        return d1[n - 1]


def to_string(*dt, sep=' ', end='\n'):
    return f"{sep}".join([str(i) for i in dt]) + end


def order(*coffe):
    global in_stock
    recept = {"Эспрессо": {"coffee": 1},
              "Капучино": {"coffee": 1, "milk": 3},
              "Макиато": {"coffee": 2, "milk": 1},
              "Кофе по-венски": {"coffee": 1, "cream": 2},
              "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
              "Кон Панна": {"coffee": 1, "cream": 1}
              }
    for i in coffe:
        fl = True
        v = recept[i]
        for ingred in recept[i]:
            if in_stock[ingred] < recept[i][ingred]:
                fl = False
                break
        if fl:
            for ingred in recept[i]:
                in_stock[ingred] -= recept[i][ingred]
            return i
    return 'К сожалению, не можем предложить Вам напиток'


def enter_results(*numbr):
    global sp
    sp += numbr


def get_sum():
    return round(sum(sp[::2]), 2), round(sum(sp[1::2]), 2)


def get_average():
    return round(2 * get_sum()[0] / len(sp), 2), round(2 * get_sum()[1] / len(sp), 2)


sp = []
string = 'Яндекс использует Python во многих проектах'


# print(sorted(string.split(), key=lambda st: (len(st), st.lower())))


def func(x):
    for i in str(x):
        if int(i) % 2 == 0:
            return True
        else:
            return False


# print(list(map(int, '123')))
# print(*filter(lambda x: sum(map(int, str(x))) % 2 == 0, (32, 64, 128, 256, 512)))


def secret_replace(s, **dict):
    res = ''
    ndict = {key: (zn, 0) for key, zn in dict.items()}
    for i in s:
        if i in ndict:
            res += ndict[i][0][ndict[i][1] % len(ndict[i][0])]
            ndict[i] = ndict[i][0], ndict[i][1] + 1
        else:
            res += i
    return res


result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
print(result)
