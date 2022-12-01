def is_part_of_linear_func(x: int, y: int, f) -> bool:
    return f(x) == y


f = lambda x: 2 * x + 3
print(is_part_of_linear_func(1, 5, f))