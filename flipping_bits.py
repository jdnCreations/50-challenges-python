def flip_bits(value):
    # 8 hex F's == 32 binary 1s
    # return value ^ 0b11111111111111111111111111111111
    return value ^ 0xFFFFFFFF


print(flip_bits(0))
print(flip_bits(2147483647))
print(flip_bits(1))
print(flip_bits(4))
