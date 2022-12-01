from typing import Union


def root_of(num: Union[int, float], pow: int) -> float:
    return num ** (1/pow)


def square_root(num: Union[int, float], epsilon: float) -> float:
    a = 1.
    b = num
    while abs(a-b) >= epsilon:
        a = (a+b) / 2
        b = num / a
    
    return a

num = 26
power = 2
print(root_of(num, power))

epsilon = 0.000001
print(square_root(num, epsilon))