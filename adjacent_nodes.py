matrix_one = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
]

matrix_two = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]


def is_adjacent(matrix, node1, node2):
    return bool(matrix[node1][node2])


print(is_adjacent(matrix_one, 0, 1))
print(is_adjacent(matrix_one, 0, 2))
print(is_adjacent(matrix_one, 2, 1))

print(is_adjacent(matrix_two, 0, 3))
print(is_adjacent(matrix_two, 1, 4))
print(is_adjacent(matrix_two, 3, 2))
