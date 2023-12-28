ints = [1, 2, 3, 4, 5]

print([i for i in ints if i % 2 == 0] + [i for i in ints if i % 2 == 1])