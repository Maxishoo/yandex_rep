import itertools
n = int(input())
alphabet_list = []
for i in range(n):
    alphabet_list.append(input().split("-"))
    alphabet_list[i] = sorted(set(alphabet_list[i]))

for symbol_tuple in itertools.product(*alphabet_list):
    word = ""
    for symbol in symbol_tuple:
        if symbol not in word:
            word = word + symbol
    if len(word) == n:
        print(word)