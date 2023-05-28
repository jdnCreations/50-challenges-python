vowels = {"a", "e", "i", "o", "u"}


def count_vowels_in_string(string):
    count = 0
    for letter in string.lower():
        if letter in vowels:
            count = count + 1
    return count


print(count_vowels_in_string("bAaaulls"))
