def pluralize(word_list):
    words = {}
    # loop over words in list,
    for word in word_list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    new_list = []
    for word in words:
        if words[word] > 1:
            new_list.append(word + "s")
        else:
            new_list.append(word)
    return new_list


print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))
