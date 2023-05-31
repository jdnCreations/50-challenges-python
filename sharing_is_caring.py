def check(val):
    # if value after decimal is 0, we can convert to int
    if int(str(val).split('.')[1]) == 0:
        return False
    return True


def show_the_love(list_of_nums):
    show_decimals = None

    # new list to return
    updated_list_of_nums = list_of_nums.copy()

    # get the smallest number
    smallest_number = min(list_of_nums)
    smallest_index = list_of_nums.index(smallest_number)

    # remove 25% from every number except the smallest
    quarter = 0.25
    removed_total = 0
    for i in range(len(list_of_nums)):
        if list_of_nums[i] != smallest_number:
            quarter_of_num = quarter * list_of_nums[i]
            removed_total += quarter_of_num

            if not show_decimals:
                show_decimals = check(list_of_nums[i] - quarter_of_num)

            if show_decimals is None:
                show_decimals = check(list_of_nums[i] - quarter_of_num)

            updated_list_of_nums[i] = list_of_nums[i] - quarter_of_num

    # add removed amount to the smallest number
    updated_list_of_nums[smallest_index] = smallest_number + removed_total

    # if show_decimals is False, convert list to ints
    if not show_decimals:
        for i in range(len(updated_list_of_nums)):
            updated_list_of_nums[i] = int(updated_list_of_nums[i])

    # return list
    return updated_list_of_nums


print(show_the_love([4, 1, 4]))  # [3, 3, 3,]
print(show_the_love([16, 10, 8]))  # [12.0, 7.5, 14.5]
print(show_the_love([2, 100]))  # [27, 75]
print(show_the_love([75, 64, 55]))  # [56.25, 48.0, 89.75]
print(show_the_love([84, 94, 26, 80, 16]))  # [63.0, 70.5, 19.5, 60.0, 87.0]
print(show_the_love([55, 27]))  # [41.25, 40.75]
print(show_the_love([13, 80, 75, 45, 11]))  # [9.75, 60.0, 56.25, 33.75, 64.25]
print(show_the_love([48, 28, 18]))  # [36.0, 21.0, 37.0]
print(show_the_love([17, 9]))  # [12.75, 13.25]
print(show_the_love([38, 23, 31, 16]))  # [28.5, 17.25, 23.25, 39.0]
print(show_the_love([54, 62, 59]))  # [84.25, 46.5, 44.25]
print(show_the_love([44, 46]))  # [55.5, 34.5])
print(show_the_love([21, 97, 45, 58]))  # [71.0, 72.75, 33.75, 43.5]
print(show_the_love([43, 9]))  # [32.25, 19.75])
print(show_the_love([53, 0, 14, 58]))  # [39.75, 31.25, 10.5, 43.5])
print(show_the_love([16, 19, 42, 43, 6]))  # [12.0, 14.25, 31.5, 32.25, 36.0])
print(show_the_love([26, 17, 28, 31, 79]))  # [19.5, 58.0, 21.0, 23.25, 59.25])
print(show_the_love([47, 57, 18, 2, 72]))  # [35.25, 42.75, 13.5, 50.5, 54.0])
