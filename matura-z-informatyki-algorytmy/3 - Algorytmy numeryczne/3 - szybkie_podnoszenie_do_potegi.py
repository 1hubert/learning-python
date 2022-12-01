from typing import Union


def quick_power_of(num: int, pow: int) -> Union[int, float]:
    if pow == 0:
        return 1

    is_pow_negative = False
    if pow < 0:
        pow = abs(pow)
        is_pow_negative = True

    result = 1
    while pow > 1:
        if pow % 2 == 1:
            result *= num
        
        num *= num
        pow = pow // 2

    if is_pow_negative:
        return 1 / (result * num)
    else:
        return result * num


def szybka_potega_rekurencyjnie(a, n):
    if n == 0:
        return 1
    if n%2 == 1:
        return a * szybka_potega_rekurencyjnie(a, n-1)

    w = szybka_potega_rekurencyjnie(a, n/2)

    return w*w


print(quick_power_of(2, 0))
