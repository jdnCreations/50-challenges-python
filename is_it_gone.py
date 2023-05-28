def find_it(items, name):
    if name not in items:
        return name.capitalize() + " is here!"
    else:
        return name.capitalize() + " is gone..."


print(find_it({"tv": 30, "stereo": 50}, "rocky"))
print(find_it({"jerome": 5, "blanket": 20}, "jerome"))
