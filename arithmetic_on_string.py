def perform_arithmetic(string):
    split_str = string.split(" ")
    first_val, operator, second_val = split_str

    first_val = int(first_val)
    second_val = int(second_val)

    if operator == "*":
        return first_val * second_val
    if operator == "+":
        return first_val + second_val
    if operator == "-":
        return first_val - second_val
    if operator == "//":
        if second_val == 0:
            return -1
        return first_val / second_val
    else:
        return "Invalid operator"


print(perform_arithmetic("12 + 12"))
print(perform_arithmetic("12 - 12"))
print(perform_arithmetic("12 * 12"))
print(perform_arithmetic("12 // 0"))
