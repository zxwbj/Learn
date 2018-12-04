import json

filename = 'numbers.json'
with open(filename) as f:
    number = json.load(f)
print(number)
