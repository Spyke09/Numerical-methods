from math import *

ro = (lambda x: 1 / sqrt(1 - x ** 2))
xk = (lambda k, n: cos((2 * k - 1) * pi / (2 * n)))
ak = (lambda k, n: pi / n)


def integrate(f, n):
    res = 0
    for k in range(1, n + 1):
        res += ak(k, n) * f(xk(k, n))
    return res


f1 = lambda x: sin(x) ** 2
f2 = lambda x: exp(-x ** 2)
f3 = lambda x: log(x ** 2 + 10) + cos(4.2 * x)

m = 10
print("f1: ", integrate(f1, m))
print("f2: ", integrate(f2, m+1))
print("f3: ", integrate(f3, m+2))

