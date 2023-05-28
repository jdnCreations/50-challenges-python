def repeat_characters_amount(base_string, amount):
    repeated_string = ""
    for char in base_string:
        repeated_string = repeated_string + (char * amount)

    return repeated_string


def repeat_characters(base_string):
    repeated_string = ""
    for char in base_string:
        repeated_string = repeated_string + (char * 2)

    return repeated_string


print(repeat_characters("FROGS"))
print(repeat_characters_amount("frogs", 4))
