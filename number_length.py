def number_length(num):
    num_str = str(num)
    length = 0
    for i in num_str:
        length += 1
    return length


print(number_length(223))