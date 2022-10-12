from math import *


def integrate(f, a, b, n):
    res = f(a) + f(b)
    h = (b - a) / n
    for k in range(1, n // 2):
        res += 2 * f(a + h * 2 * k)
    for k in range(1, n // 2 + 1):
        res += 4 * f(a + h * (2 * k - 1))
    return res * h / 3


f1 = lambda x: sin(x) ** 2
f2 = lambda x: exp(-x ** 2)
f3 = lambda x: log(x ** 2 + 10) + cos(4.2 * x)

m = 100
print("f1: ", integrate(f1, 0, 10, m))
print("f2: ", integrate(f2, 0, 10, m+1))
print("f3: ", integrate(f3, 0, 10, m+2))


