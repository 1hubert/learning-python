from operator import truediv


def triangle_check(a, b, c) -> bool:
    if max(a, b, c) == c:
        if a + b > c:
            return True
    elif max(a, b, c) == b:
        if a + c > b:
            return True
    elif max(a, b, c) == a:
        if b + c > a:
            return True
    return False


print(triangle_check(2, 3, 5))