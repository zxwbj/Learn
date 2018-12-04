
import name_function

print("Enter 'q' at any time to quit.")
while True:
    first = input("Please give me a first name: ")
    if 'q' == first:
        break
    last = input("Please give me a last name: ")
    if 'q' == last:
        break

    formatted_name = name_function.get_formatted_name(first, last)
    print("\tNeatly formatted name: {}.".format(formatted_name))
