operators = {"*", "/", "-", "+"}


def calculate(integer1, operator, integer2):
    if operator not in operators:
        return "Invalid operator"
    if operator == "*":
        return integer1 * integer2
    if operator == "/":
        return integer1 / integer2
    if operator == "-":
        return integer1 - integer2
    if operator == "+":
        return integer1 + integer2


print(calculate(5, "+", 3))
print(calculate(2, "*", 3))
print(calculate(9, "-", 2))
print(calculate(10, "/", 5))
print(calculate(2, ".", 3))
