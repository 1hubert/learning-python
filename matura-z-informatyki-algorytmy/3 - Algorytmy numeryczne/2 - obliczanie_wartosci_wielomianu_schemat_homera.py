from typing import List


def horner_recursively(wsp: List[int], st: int, x: int) -> int:
    if st == 0:
        return wsp[0]

    return x * horner_recursively(wsp, st-1, x) + wsp[st]


def horner_iteratively(wsp: List[int], st: int, x: int) -> int:
    result = wsp[0]
    
    for i in range(1, st+1):
        result = result*x + wsp[i]

    return result


wspolczynniki = [1, 1, 1, 10]
stopien = 3
x = 1

result = horner_iteratively(wspolczynniki, stopien, x)
print(result)
