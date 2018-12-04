import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What's your name? ")
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("welcome back, " + username)
    else:
        username = get_new_username()
        print("welcome, " + username)


if '__main__' == __name__:
    greet_user()
