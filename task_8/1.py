import numpy as np


def gauss_solve(a1: np.matrix, f: np.matrix):
    a = np.matrix(a1)
    x = np.matrix(f)
    n = a.shape[0]
    for i in range(n):
        # выбор ведущего элемента
        k = i
        for j in range(i+1, n):
            if abs(a[j, i]) > abs(a[k, i]):
                k = j
        for j in range(n):
            a[i, j], a[k, j] = a[k, j], a[i, j]
        for j in range(x.shape[1]):
            x[i, j], x[k, j] = x[k, j], x[i, j]
        # прямой ход
        x[i] /= a[i, i]
        a[i] /= a[i, i]
        for j in range(i + 1, n):
            x[j] -= x[i] * a[j, i]
            a[j] -= a[i] * a[j, i]
    # обраный ход
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            x[j] -= x[i] * a[j, i]
            a[j] -= a[i] * a[j, i]
    return x


def test():
    a = np.matrix(np.random.uniform(-12, 12, (5, 5)))
    f = np.matrix(np.random.uniform(-12, 12, (5, 1)))
    x = gauss_solve(a, f)
    print(a * x)
    print(np.linalg.norm(a * x - f))


test()
