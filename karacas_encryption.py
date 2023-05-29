chart = {
    "a": "0",
    "e": "1",
    "i": "2",
    "o": "2",
    "u": "3"
}


def replace_vowels(str_to_replace):
    new_str = ''
    # loop over characters in string
    for char in str_to_replace:
        # check if character is a vowel
        if char in chart:
            # replace with corresponding value
            new_str += chart[char]
        else:
            new_str += char

    return new_str


def acafy(str_to_acafy):
    new_str = str_to_acafy + "aca"
    return new_str


def encrypt(value):
    reversed_str = reversed(value)
    replaced = replace_vowels(reversed_str)
    acafied = acafy(replaced)
    return acafied


print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("burak"))
print(encrypt("alpaca"))
