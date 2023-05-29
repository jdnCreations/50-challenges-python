def snakefill(grid):
    grid_size = grid * grid
    snake_size = 1
    eat_count = 0

    while snake_size < grid_size:
        snake_size *= 2
        if snake_size >= grid_size:
            return eat_count
        eat_count += 1
    return eat_count


print(snakefill(3))
print(snakefill(6))
print(snakefill(24))
