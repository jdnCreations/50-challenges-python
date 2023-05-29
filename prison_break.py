# cell contains one prisoner
# 1 = unlocked, 0 = locked


def free(list_of_cells, cell):
    return list_of_cells[cell] == 1


def flip_cells(list_of_cells):
    for i in range(len(list_of_cells)):
        list_of_cells[i] ^= 1
    return list_of_cells


def freed_prisoners(list_of_cells):
    copied_list = list_of_cells.copy()
    amount_freed = 0

    if not free(copied_list, 0):
        return 0

    for i in range(len(list_of_cells)):
        if free(copied_list, i):
            amount_freed += 1
            flip_cells(copied_list)
    return amount_freed


print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))
print(freed_prisoners([1, 0, 0, 0, 0, 0, 0]))
print(freed_prisoners([1, 0, 1, 0, 1, 0]))
print(freed_prisoners([1, 1, 1]))
print(freed_prisoners([0, 0, 0]))
print(freed_prisoners([0, 1, 1, 1]))
