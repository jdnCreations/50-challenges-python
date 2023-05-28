def time_saved(speed_limit, avg_speed, distance_travelled_at_avg_speed):
    normal_speed = distance_travelled_at_avg_speed / speed_limit
    speeding = distance_travelled_at_avg_speed / avg_speed
    return round(abs(normal_speed - speeding) * 60, 1)


print(time_saved(80, 90, 40))
print(time_saved(80, 90, 4000))
