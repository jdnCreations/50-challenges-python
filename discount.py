def get_discounted_price(price, discount):
    return 100 - (discount / 100) * price


print(get_discounted_price(100, 20))
