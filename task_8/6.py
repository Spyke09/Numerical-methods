import math
from math import sin, factorial
from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as plt


def get_teilor_coef(f, n):
    coef = list()
    for i in range(n + 1):
        coef.append(derivative(f, 0, dx=1E-2, n=i, order=6 * (n + 1) + 5) / factorial(i))
    return coef


def pade_approximation(f, m, n):
    c = get_teilor_coef(f, m + n)
    print(c)
    mat = np.zeros((n, n))
    f1 = np.zeros(n)
    for i in range(n):
        for j in range(n):
            mat[i, j] = -c[m - n + 1 + i + j]
        f1[i] = c[m + 1 + i]
    b = np.flip(np.linalg.solve(mat, f1))
    b = np.concatenate((np.array([1]), b))
    a = np.zeros(m + 1)
    for i in range(m + 1):
        a[i] = sum(c[j] * b[i - j] if i - j <= n else 0 for j in range(i + 1))
    print(a, b, sep='\n')
    return a, b


def get_value(coef, x):
    a, b = coef
    c, z = 0, 0
    for i, ai in enumerate(a):
        c += ai * x ** i
    for i, bi in enumerate(b):
        z += bi * x ** i
    return c / z


def test1(x0, x1, n):
    num = 1000
    f = lambda x: 1 / (sin(x ** 2) + 1)
    x = np.linspace(x0, x1, num)
    y = np.zeros(num)
    m = n - 1
    coef = pade_approximation(f, m, n)
    for i in range(num):
        y[i] = get_value(coef, x[i])

    plt.plot(x, y)
    for i in range(num):
        y[i] = f(x[i])
    plt.plot(x, y)
    plt.show()


def test2(x0, x1, n):
    num = 1000
    f = lambda x: math.sinh(x)
    x = np.linspace(x0, x1, num)
    y = np.zeros(num)
    m = n + 2
    coef = pade_approximation(f, m, n)
    for i in range(num):
        y[i] = get_value(coef, x[i])

    plt.plot(x, y)
    for i in range(num):
        y[i] = f(x[i])
    plt.plot(x, y)
    plt.show()


def test3(x0, x1, n):
    num = 1000
    f = lambda x: math.sqrt((1 + 0.5 * x) / (1 + 2 * x))
    x = np.linspace(x0, x1, num)
    y = np.zeros(num)
    m = n + 2
    coef = pade_approximation(f, m, n)
    for i in range(num):
        y[i] = get_value(coef, x[i])

    plt.plot(x, y)
    for i in range(num):
        y[i] = f(x[i])
    plt.plot(x, y)
    plt.show()


test1(-1, 1, 2)
test2(-4, 4, 5)
test3(0, 4, 2)
