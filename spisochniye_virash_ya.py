# n = 3
# print([[j * i for j in range(1, n + 1)] for i in range(1, n + 1)])

# sentence = 'Мама мыла раму'
# print([len(i) for i in sentence.split()])

# numbers = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
# print({i for i in numbers if i % 2 != 0})

# numbers = [number for number in range(16, 100, 4)]
# print({i for i in numbers if (int(i ** 0.5)) ** 2 == i})

# text = 'Мама мыла раму!'
# print({letter: text.lower().count(letter) for letter in text.lower().replace(' ', '') if letter.isalpha()})

# numbers = {1, 2, 3, 4, 5}
# print({i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers})

# string = 'открытое акционерное общество'
# print(''.join([i[0].upper() for i in string.split()]))

numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]
print(' - '.join([str(i) for i in sorted(set(numbers))]))

rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
print(''.join([letter * count for letter, count in rle]))
