import json

filename = "username.json"
try:
    with open(filename) as f:
        name = json.load(f)
except FileNotFoundError:
    name = input("pls input your name: ")
    with open(filename, 'w') as f:
        json.dump(name, f)
    print("Welcome, {}.".format(name))
else:
    print("Welcome back, {}.".format(name))
