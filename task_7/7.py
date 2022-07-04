from math import *


def getAk(n):
    if n == 1:
        return [0.88662692, ]
    if n == 2:
        return [0.72336302, 0.72336302]
    if n == 3:
        return [0.56718628, 0.30537111, 0.01366888]
    else:
        return None


def getXk(n):
    if n == 1:
        return [1.5, ]
    if n == 2:
        return [0.91886117, 4.0811388]
    if n == 3:
        return [0.66632591, 2.8007750, 7.0328990]
    else:
        return None


def integrate(f, n):
    res = 0
    a = getAk(n)
    x = getXk(n)
    for k in range(n):
        res += a[k] * f(x[k])
    return res


f1 = lambda x: 10*sin(x/10)
f2 = lambda x: exp(-0.1*x ** 2)/10
f3 = lambda x: log(x ** 2+ 20) + cos(x/10)

m = 3
print("f1: ", integrate(f1, m))
print("f2: ", integrate(f2, m))
print("f3: ", integrate(f3, m))
