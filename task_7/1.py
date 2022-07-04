import numpy as np


def swapLines(array, i, j):
    if i == j:
        return
    for k in range(array.shape[1]):
        t = array[i, k]
        array[i, k] = array[j, k]
        array[j, k] = t


def prepareMatrices(a, f):
    n = a.shape[0]
    for k in range(n):
        pi, qi = k, k
        for i in range(k, n):
            if abs(a[i, k]) > abs(a[pi, k]):
                pi = i
        swapLines(a, k, pi)
        swapLines(f, k, pi)


def getLUMatrices(array):
    n = array.shape[0]
    l = np.zeros([n, n])
    u = np.zeros([n, n])
    for i in range(n):
        l[i, i] = 1

    for i in range(n):
        for j in range(n):
            s = 0
            if i <= j:
                for k in range(i):
                    s += l[i, k] * u[k, j]
                u[i, j] = (array[i, j] - s)
            else:
                for k in range(j):
                    s += l[i, k] * u[k, j]
                l[i, j] = (array[i, j] - s) / u[j, j]
    return l, u


def directSubstitution(l: np.array, f: np.array):
    n = f.shape[0]
    g = np.zeros(n)
    for k in range(n):
        s = 0
        for i in range(k):
            s += l[k, i] * g[i]
        g[k] = (f[k] - s) / l[k, k]
    return g


def backSubstitution(u: np.array, g: np.array):
    n = g.shape[0]
    x = np.zeros(n)
    for k in range(n - 1, -1, -1):
        s = 0
        for j in range(k + 1, n):
            s += u[k, j] * x[j]
        x[k] = (g[k] - s) / u[k, k]
    return x


def linearSolve(a: np.array, f: np.array):
    n, m = f.shape[0], f.shape[1]
    prepareMatrices(a, f)
    l, u = getLUMatrices(a)
    res = np.zeros([n, m])
    for i in range(m):
        cur = np.zeros(n)
        for j in range(n):
            cur[j] = f[j, i]
        y = directSubstitution(l, cur)
        x = backSubstitution(u, y)
        for j in range(n):
            res[j, i] = x[j]
    return res


def test1():
    for _ in range(10):
        a = np.random.uniform(-12, 12, (5, 5))
        f = np.random.uniform(-12, 12, (5, 4))
        x = linearSolve(a, f)
        print(np.linalg.norm(a.dot(x) - f))


def test2():
    for _ in range(10):
        a = np.random.uniform(-12, 12, (5, 5))
        f = np.random.uniform(-12, 12, (5, 4))
        for i in range(a.shape[0]):
            a[i, i] = 0
        x = linearSolve(a, f)
        print(np.linalg.norm(a.dot(x) - f))


print("Обычные матрицы")
test1()
print("Матрица А с нулями на диагонали")
test2()
