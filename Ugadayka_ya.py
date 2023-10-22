print(500)
start = 1
end = 1000
s = input()
while s != "Угадал!":
    if s == 'Меньше':
        start = start
        end = (end + start) // 2 - 1
    elif s == 'Больше':
        start = (end + start) // 2 + 1
        end = end
    print((end + start) // 2)
    s = input()
