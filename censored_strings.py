def uncensor(string, censor):
    censor_list = []
    censor_list[:0] = censor
    new_str = ""
    for i in range(len(string)):
        if string[i] == "*":
            new_str = new_str + censor_list[0]
            censor_list.pop(0)
        else:
            new_str = new_str + string[i]
    return new_str


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))
