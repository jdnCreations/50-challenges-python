def get_numbers_from_list(int_and_strings):
    number_list = []
    for item in int_and_strings:
        if type(item) == int:
            number_list.append(item)

    return number_list


print(get_numbers_from_list([1, 6, 8, "string", "test", 32]))

