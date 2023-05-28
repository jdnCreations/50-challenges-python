def virtual_dac(value):
    return round((value * 5) / 1023, 2)


print(virtual_dac(400))
print(virtual_dac(0))
print(virtual_dac(1023))
