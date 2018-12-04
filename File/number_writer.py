import json
numbers = [1, 2, 4, 8, 16]

filename = "numbers.json"
with open(filename, 'w') as f:
    json.dump(numbers, f)
