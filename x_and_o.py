def equal_x_and_o(string):
    os = 0
    xs = 0
    for char in string.lower():
        if (char == 'x'):
            xs = xs + 1
        if (char == 'o'):
            os = os + 1
    return os == xs


print(equal_x_and_o("XOXOXOXXA"))
print(equal_x_and_o("XXXOOO"))
print(equal_x_and_o("xxXXoOXoXOxXXXOo"))
