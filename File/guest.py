filename = "guests.txt"

count = 0
while count < 5:
    name = input("pls enter your name: ")
    print("Hi, " + name + ".")
    with open(filename, "a") as f:
        f.write(name + "\n")
    count += 1
