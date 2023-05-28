def profit(dictionary):
    cost_price, sell_price, inventory = dictionary['cost_price'], dictionary['sell_price'], dictionary['inventory']
    total_sales = sell_price * inventory
    total_cost = cost_price * inventory
    return round(total_sales - total_cost)
