import numpy as np


def danilevsky(a):
    b = frobeniusMatrix(a)
    bab = np.linalg.inv(b) * a * b
    res = list(-np.array(b[0])[0])
    res.insert(0, 1)
    return list(reversed(res))


def frobeniusMatrix(a):
    n = a.shape[0]
    for i in range(n - 1):
        bt = np.matrix(np.eye(n))
        for j in range(n):
            bt[n - 2 - i, j] = -a[n - 1 - i, j] / a[n - 1 - i, n - 2 - i]
        bt[n - 2 - i, n - 2 - i] = 1 / a[n - 1 - i, n - 2 - i]
        a = np.linalg.inv(bt) * a * bt
    return a


def check_result(a1: np.matrix, c: list):
    res = np.matrix(np.eye(a1.shape[0])) * c[0]
    a = a1.copy()
    for i in range(1, len(c)):
        res += a * c[i]
        a = a * a1
    return res


t = np.matrix([[2.2, 1, 0.5, 2],
               [1, 1.3, 2, 1],
               [0.5, 2, 0.5, 1.6],
               [2, 1, 1.6, 2]])

coef = danilevsky(t)
print("Норма матрицы невязки - ", np.linalg.norm(check_result(t, coef)))
print(coef)
# t = np.matrix(np.random.uniform(-1, 1, (20, 20)))
# coef = danilevsky(t)
# print("Норма матрицы невязки - ", np.linalg.norm(check_result(t, coef)))
