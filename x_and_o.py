
def equal_amount_of_char(string, char1, char2):
    i = 0
    j = 0
    for char in string.lower():
        if char == char1:
            i = i + 1
        if char == char2:
            j = j + 1
    return i == j


def equal_x_and_o(string):
    os = 0
    xs = 0
    for char in string.lower():
        if char == 'x':
            xs = xs + 1
        if char == 'o':
            os = os + 1
    return os == xs


print(equal_amount_of_char("XXXOOO", "x", "o"))
print(equal_x_and_o("XOXOXOXXA"))
print(equal_x_and_o("XXXOOO"))
print(equal_x_and_o("xxXXoOXoXOxXXXOo"))
