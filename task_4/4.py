import numpy as np


def get_tr(a: np.matrix):
    res = 0
    n = a.shape[0]
    for i in range(n):
        res += a[i, i]
    return res


def get_coef(a1: np.matrix):
    a = a1.copy()
    n = a.shape[0]
    res = [1, ]
    id = np.matrix(np.eye(n))
    for i in range(n):
        q = get_tr(a) / (i + 1)
        t = q*id
        b = a - q * id
        a = a1 * b
        res.append(-q)
    res.reverse()
    return res

def check_result(a1: np.matrix, c: list):
    res = np.matrix(np.eye(a1.shape[0]))*c[0]
    a = a1.copy()
    for i in range(1, len(c)):
        res += a*c[i]
        a = a*a1
    return res


t = np.matrix([[1, 0.17, -0.25, 0.54],
               [0.47, 1, 0.67, -0.32],
               [-0.11, 0.35, 1, -0.74],
               [0.55, 0.43, 0.36, 1]])

coef = get_coef(t)
print(np.linalg.norm(check_result(t, coef)))
print(coef)
# t = np.matrix(np.random.uniform(-1, 1, (20, 20)))
# coef = get_coef(t)
# print(np.linalg.norm(check_result(t, coef)))