import math
import numpy as np
import matplotlib.pyplot as plt


def get_points(x0: float, x1: float, n: int):
    x = np.linspace(x0, x1, n)
    y = np.random.uniform(x0, x1, n)
    return x, y


def get_points_from_func(x0: float, x1: float, n: int, f):
    x = np.linspace(x0, x1, n)
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(x[i])
    return x, y


def fiN(x: np.array, y: np.array, n: int):
    res = 0
    for j in range(n+1):
        p = 1
        for i in range(n+1):
            if i != j:
                p *= (x[j] - x[i])
        res += y[j]/p
    return res


def interpolation(points: tuple, x0: float):
    x, y = points
    res = y[0]
    n = x.shape[0]-1
    d = 1
    for k in range(n):
        d *= (x0 - x[k])
        res += d * fiN(x, y, k+1)
    return res


def test1(n):
    p = get_points(-2, 2, n, )
    plt.scatter(*p)
    x = np.linspace(-2, 2, 10 * n)
    y = np.zeros(10 * n)
    for i in range(10 * n):
        y[i] = interpolation(p, x[i])
    plt.plot(x, y)
    plt.show()


def test2(n):
    x0, x1 = 0, 2
    f = lambda x: math.sin(9*x)+math.log(x*x+9)
    p = get_points_from_func(x0, x1, n, f)
    plt.plot(*get_points_from_func(x0, x1, 10*n, f))
    x = np.linspace(x0, x1, 10 * n)
    y = np.zeros(10 * n)
    for i in range(10 * n):
        y[i] = interpolation(p, x[i])
    plt.plot(x, y)
    plt.show()


test2(9)