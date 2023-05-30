rate1 = {
    'people': 4,
    'walls': 9,
    'minutes': 63
}
rate2 = {
    'people': 10,
    'walls': 10,
    'minutes': 22
}


def time(rate, people, walls):
    """
        minutes = k * walls / people

        63 minutes for 4 people to paint 9 walls
        63 = 9k/4
        252 = 9k
        28 = k
    """
    k = rate['minutes'] * rate['people']
    k = k / rate['walls']
    return (k * walls) / people


print(time(rate1, 7, 4))
print(time(rate2, 10, 10))
