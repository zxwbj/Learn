while True:
    first_number = input("First number: ")
    second_number = input("Second number:")
    if 'q' == first_number or 'q' == second_number:
        break
    try:
        ans = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Can't divide by 0.")
    else:
        print(ans)
