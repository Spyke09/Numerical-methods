import numpy as np


def swap(a: np.array, i, j, axis=0):
    if axis == 0:
        for k in range(a.shape[1]):
            temp = a[i, k]
            a[i, k] = a[j, k]
            a[j, k] = temp
    if axis == 1:
        for k in range(a.shape[0]):
            temp = a[k, i]
            a[k, i] = a[k, j]
            a[k, j] = temp


def get_q(a: np.array, f: np.array):
    n = a.shape[0]
    q = [0 for i in range(n)]
    for k in range(n):
        pi, qi = k, k
        for i in range(k, n):
            if abs(a[i, k]) > abs(a[pi, k]):
                pi = i
        q[k] = int(qi)
        swap(a, k, pi, 0)
        swap(f, k, pi, 0)
    return q


def get_lu(a: np.array):
    n = a.shape[0]
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
                u[i, j] = (a[i, j] - s)
            else:
                for k in range(j):
                    s += l[i, k] * u[k, j]
                l[i, j] = (a[i, j] - s) / u[j, j]
    return l, u


def direct_sub(l: np.array, f: np.array):
    n = f.shape[0]
    g = np.zeros(n)
    for k in range(n):
        s = 0
        for i in range(k):
            s += l[k, i] * g[i]
        g[k] = (f[k] - s) / l[k, k]
    return g


def back_sub(u: np.array, g: np.array):
    n = g.shape[0]
    x = np.zeros(n)
    for k in range(n - 1, -1, -1):
        s = 0
        for j in range(k + 1, n):
            s += u[k, j] * x[j]
        x[k] = (g[k] - s) / u[k, k]
    return x


def lu_solve(a: np.array, f: np.array):
    p = get_q(a, f)
    n, m = f.shape[0], f.shape[1]
    l, u = get_lu(a)
    # print(l)
    # print(u)
    res = np.zeros([n, m])
    for i in range(m):
        cur = np.zeros(n)
        for j in range(n):
            cur[j] = f[j, i]
        y = direct_sub(l, cur)
        x = back_sub(u, y)
        for j in range(n):
            res[j, i] = x[j]
    res = np.array([res[p[i]] for i in range(n)])
    return res


# for _ in range(10):
#     a = np.random.uniform(-12, 12, (5, 5))
#     f = np.random.uniform(-12, 12, (5, 4))
#     x = lu_solve(a, f)
#     print(np.linalg.norm(a.dot(x) - f))

a = np.random.uniform(-12, 12, (5, 5))
f = np.random.uniform(-12, 12, (5, 4))
for i in range(a.shape[0]):
    a[i, i] = 0
x = lu_solve(a, f)
print(np.linalg.norm(a.dot(x) - f))