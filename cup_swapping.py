def cup_swapping(swap_list):
    # positions
    positions = ["A", "B", "C"]
    ball_position = positions[1]

    for item in swap_list:
        # if swap item contains ball_position
        if ball_position in item:
            pos1 = item[0]
            pos2 = item[1]

            # if pos1 is not ball position
            if pos1 != ball_position:
                # move ball_position to pos1
                ball_position = pos1
            else:
                # pos2 is ball position
                ball_position = pos2

    return ball_position


print(cup_swapping(['AB', 'CA']))  # 'C')
print(cup_swapping(['AB', 'CA', 'AB']))  # 'C')
print(cup_swapping(['AC', 'CA', 'CA', 'AC']))  # 'B')
print(cup_swapping(['BA', 'AC', 'CA', 'BC']))  # 'A')
print(cup_swapping(['BC', 'CB', 'CA', 'BA']))  # 'A')
print(cup_swapping(['BC']))  # 'C')
print(cup_swapping(['BA', 'CA', 'CB', 'CA']))  # 'B')
print(cup_swapping([]))  # 'B')
