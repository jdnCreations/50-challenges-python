def repeat_characters_amount(base_string, amount):
    repeated_string = ""
    for char in base_string:
        repeated_string = repeated_string + (char * amount)

    return repeated_string


def repeat_characters(base_string):
    return repeat_characters_amount(base_string, 1)


print(repeat_characters("FROGS"))
print(repeat_characters_amount("frogs", 4))
