import math
from math import sqrt, pi, exp, factorial, sin
import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt


fi = [(lambda x: 1),
      (lambda x: 2 * x),
      (lambda x: 4*x ** 2 - 2),
      (lambda x: 8*x ** 3 - 12 * x),
      (lambda x: 16*x ** 4 - 48 * x ** 2 + 12),
      (lambda x: 32*x ** 5 - 160 * x ** 3 + 120 * x),
      (lambda x: 64*x ** 6 - 480 * x ** 4 + 720 * x ** 2 - 120)]

r = lambda x: exp(-x ** 2)
norm = lambda n: 1/(2**n * factorial(n)*sqrt(pi))

def approximation(f, n):
    global fi, r
    n = min(7, n)
    res = list()
    for i in range(n):
        cur_int = integrate.quad(lambda x: r(x)*fi[i](x)*f(x)*norm(i), -100, 100)
        res.append(cur_int[0])
    return res

def get_value(a, x, n):
    res = 0
    n = min(7, n)
    global fi
    for i in range(n):
        res += a[i]*fi[i](x)
    return res

def test1(x0, x1, n):
    f = lambda x: 5*sin(x)+sin(20*x)
    x = np.linspace(x0, x1, n)
    y = np.zeros(n)
    m = 7
    coef = approximation(f, m)
    for i in range(n):
        y[i] = get_value(coef, x[i], m)
    plt.plot(x, y)
    for i in range(n):
        y[i] = f(x[i])
    plt.plot(x, y)
    plt.show()

def test2(x0, x1, n):
    f = lambda x: math.sinh(x)/20+0.4*sin(20*x)
    x = np.linspace(x0, x1, n)
    y = np.zeros(n)
    m = 7
    coef = approximation(f, m)
    for i in range(n):
        y[i] = get_value(coef, x[i], m)
    plt.plot(x, y)
    for i in range(n):
        y[i] = f(x[i])
    plt.plot(x, y)
    plt.show()

test1(-4, 4, 1000)
test2(-5, 5, 1000)