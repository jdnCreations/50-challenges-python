def hide_number(card_number):
    asterisks = (len(card_number) - 4) * "*"
    return asterisks + str(card_number[-4:])


print(hide_number("5218888888884444"))
print(hide_number("8882388558883244"))
