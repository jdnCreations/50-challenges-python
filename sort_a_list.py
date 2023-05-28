my_list = [1, 12, 8, 7, 33, 261, 2]


def swap(val1, val2):
    tmp = val1
    val1 = val2
    val2 = tmp
    return [val1, val2]


def ascending(list_of_numbers):
    new_list = list_of_numbers.copy()
    # loop over list
    for i in range(0, len(new_list)):
        for j in range(i + 1, len(new_list)):
            if new_list[i] > new_list[j]:
                new_list[i], new_list[j] = swap(new_list[i], new_list[j])
    return new_list


def descending(list_of_numbers):
    new_list = list_of_numbers.copy()
    # loop over list
    for i in range(0, len(new_list)):
        for j in range(i + 1, len(new_list)):
            if new_list[i] < new_list[j]:
                new_list[i], new_list[j] = swap(new_list[i], new_list[j])
    return new_list


def sort_numbers(list_of_numbers, sort_type):
    sort_type = sort_type.lower()
    if sort_type == "none":
        return list_of_numbers
    if sort_type == "asc":
        return ascending(list_of_numbers)
    if sort_type == "desc":
        return descending(list_of_numbers)
    else:
        return "Incorrect parameters: valid sort types are 'asc', 'desc', or 'none'"


print(sort_numbers(my_list, "asc"))
print(sort_numbers(my_list, "desc"))
print(sort_numbers(my_list, "none"))
print(sort_numbers([2, 1], "frog"))
