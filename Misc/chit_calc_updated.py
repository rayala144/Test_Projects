sum_arr, data = [], {}
strength = int(input('Strength: '))
for i in range(1, strength + 1):
    k = int(input(f'{i}. '))
    data[str(i)] = k


def calc_chit(length: int):
    # #to get integer list
    # integer_list = list(map(int, input().split()))
    # to get char or str list, just replace int with str
    str_list = list(map(str, input('Enter digits: ').split()))
    num_list = [str(num) for num in range(1, length + 1)]
    # syntax of map(): map(dataType, iterable [, iterable2, iterable3,...iterableN])
    temp_sum = 0
    count = 0
    for digit in str_list:
        if digit in num_list:
            count += 1
            temp_sum += data[digit]
        else:
            temp_sum = 0
            print(f"character '{digit}' is invalid")
            break

    if count == len(str_list):
        print(temp_sum)

    if temp_sum > 0:
        sum_arr.append(temp_sum)

    print("Total: ", sum(sum_arr))
    return


while True:
    calc_chit(strength)
