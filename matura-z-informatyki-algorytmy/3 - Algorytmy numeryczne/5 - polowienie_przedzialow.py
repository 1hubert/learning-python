def f(x):
    return (4 * (x**3)) - (1 * (x**2)) - (3 * x) + 2


def polowienie(a, b):
    epsilon = 0.000001

    if f(a) == 0:
        return a
    if f(b) == 0:
        return b

    while b-a > epsilon:
        s = (a+b) / 2

        if f(s) == 0:
            return s
        if f(a) * f(s) < 0:
            b = s
        else:
            a = s
        
    return (a+b) / 2


print(polowienie(-10, 10))