import math
import numpy as np


def minMaxEigenvalues(a):
    ev = np.linalg.eig(a)[0]
    return min(ev), max(ev)


def getAlpha(mat, l):
    a, b = minMaxEigenvalues(mat)
    t = [math.cos((k + 0.5) / l) for k in range(l)]
    ak = [1 / ((a + b) / 2 + (b - a) / 2 * t[k]) for k in range(l)]
    return ak


def linearSolve(a, f, l):
    a = np.matrix(a)
    alpha = getAlpha(a, l)
    n = a.shape[0]
    i, x = np.eye(n), np.zeros(n)
    for k in range(l):
        x = np.array(i - alpha[k] * a).dot(x) + alpha[k] * f
    return x


def test1():
    d = dict()
    for _ in range(10):
        a = np.random.uniform(-12, 12, (5, 5))
        a = a.dot(a.transpose())
        f = np.random.random(5)
        x = linearSolve(a, f, 10000)
        m = minMaxEigenvalues(a)
        d[int(m[1]/m[0])] = np.linalg.norm(a.dot(x) - f)
    for i in sorted(d.keys(), reverse=True):
        print(f"M/m = {i:5}, невязка = {d[i]}")


test1()
