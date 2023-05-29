def remove_letters(list_of_letters, string):
    for letter in string:
        if letter in list_of_letters:
            list_of_letters.remove(letter)
    return list_of_letters


print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))
