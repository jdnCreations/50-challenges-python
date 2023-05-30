def sock_merchant(int_list):
    pairs = {}
    pair_count = 0
    for item in int_list:
        if item in pairs:
            pairs[item] = pairs[item] + 1
        else:
            pairs[item] = 1

    for val in pairs.values():
        while val >= 2:
            val -= 2
            pair_count += 1
    return pair_count


print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))
print(sock_merchant([]))
