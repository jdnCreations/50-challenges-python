def calculate_damage(damage, speed, time):
    if time == "second":
        return damage * speed
    if time == "minute":
        return damage * speed * 60
    if time == "hour":
        return damage * speed * (60 * 60)


print(calculate_damage(40, 5, "second"))
print(calculate_damage(100, 1, "minute"))
print(calculate_damage(2, 100, "hour"))
