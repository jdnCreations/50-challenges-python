def color_invert(rgb):
    red, green, blue = rgb
    return 255 - red, 255 - green, 255 - blue


print(color_invert((165, 170, 119)))
