# 1
# with open("pi_digits.txt") as f:
#     contents = f.read()
#     print(contents, end="")

# 2
# with open("pi_digits.txt") as f:
#     for line in f:
#         print(line, end="")

# 3
with open("pi_digits.txt") as f:
    #lines = f.readlines()
    lines = list(f)
print(lines)
for line in lines:
    print(line, end="")
