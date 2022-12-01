def NWD_iteracyjnie(a, b):
    while a != b:
        if a>b:
            a-=b
        else:
            b-=a
    return a


def NWD_rekurencyjnie(a, b):
    if a != b:
        if a>b:
            return NWD_rekurencyjnie(a-b, b)
        else:
            return NWD_rekurencyjnie(a, b-a)
    return a

print(NWD_iteracyjnie(2, 200))
print(NWD_rekurencyjnie(2, 200))

