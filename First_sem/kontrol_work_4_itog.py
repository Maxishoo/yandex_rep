def index(text):
    for i in sorted({simb for simb in text if simb.isalpha()}):
        yield i, text.find(i)


'''
text = "The quick brown fox jumps over a lazy dog."
for letter, i in index(text):
    print(letter, i, sep="-", end=", ")
'''


def print_weather(a, b):
    print(f"За окном дует ветер со скоростью {a} м/с. Температура воздуха {b}°C.")


ans = []


def add_number(a):
    global ans
    ans.append(str(a))


def get_prod():
    mult = 1
    global ans
    for i in ans:
        mult *= int(i)
    return ' * '.join(ans) + ' = ' + str(mult)


'''
add_number(7)
add_number(2)
print(get_prod())
add_number(5)
print(get_prod())
'''


def count_pairs(*numbers, div=10):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % div == 0:
                count += 1
    return count


def grasshopper(start, finish, length):
    res = []

    def grasshopper2(start, finish, length, way):
        if len(way) == length + 1 and start == finish:
            res.append(way)
            return 1
        if len(way) > length or start == finish:
            return 1
        grasshopper2(start + 1, finish, length, list(way) + [start + 1])
        grasshopper2(start + 2, finish, length, list(way) + [start + 2])
        grasshopper2(start - 1, finish, length, list(way) + [start - 1])
        grasshopper2(start - 2, finish, length, list(way) + [start - 2])

    grasshopper2(start, finish, length, [start])
    return res


result = grasshopper(2, 5, 3)
print(*result, sep="\n")
