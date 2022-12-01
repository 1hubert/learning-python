def silnia_rekurencyjnie(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * silnia_rekurencyjnie(num-1)


def silnia_instrukcja(num: int) -> str:
    result = 1
    string = str(num)
    while num > 1:
        result = result * num
        string += f' * {num-1}'
        num -= 1
    string += f' = {result}'
    return string


num = 3
#print(silnia_instrukcja(num))
print(silnia_rekurencyjnie(num))
