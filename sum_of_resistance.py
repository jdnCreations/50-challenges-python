def series_resistance(array):
    resistance = 0
    for value in array:
        resistance += value
    print(str(resistance) + ohm_or_ohms(resistance))


def ohm_or_ohms(value):
    if value > 1:
        return " ohms"
    else:
        return " ohm"


series_resistance([1, 5, 6, 3])
series_resistance([16, 3.5, 6])
series_resistance([0.5, 0.5])
