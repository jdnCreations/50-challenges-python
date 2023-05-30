def convert_to_hex(string):
    converted = ""
    for char in string:
        converted = converted + format(ord(char), "x") + " "
    return converted.rstrip()
