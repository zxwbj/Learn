
def plus_one(arr):
    num = len(arr) - 1

    while num > -1:
        if arr[num] == 9:
            arr[num] = 0
            num = num - 1
        else:
            arr[num] = arr[num] + 1
            return arr

    new_arr = [0 for _ in range(len(arr) + 1)]
    new_arr[0] = 1
    return new_arr


if '__main__' == __name__:
    print(plus_one([1]))
    print(plus_one([1, 2, 3]))
    print(plus_one([3, 2, 9]))
    print(plus_one([9, 9, 9]))
    print(plus_one([9, 9, 9, 9, 9]))
