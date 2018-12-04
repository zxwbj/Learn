
with open("pi_digits.txt") as f:
    lines = f.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print("length of pi_string: {}".format(len(pi_string)))
