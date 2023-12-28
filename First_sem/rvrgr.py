from sys import stdin
import json

sequence = [int(i) for i in stdin]
result_dict = {}

for number in sequence:
    for digit in str(number):
        if digit not in result_dict:
            result_dict[digit] = [number]
        else:
            result_dict[digit].append(number)

with open('result.json', 'w') as file:
    json.dumps(result_dict, file, indent=4)
