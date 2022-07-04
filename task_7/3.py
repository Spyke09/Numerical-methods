import numpy as np


def additionalPoints(x):
    n = x.shape[0]
    a = np.array([2 * np.random.random(n) - 1 for _ in range(n)])
    return np.array([x + a[i] for i in range(n)])


def hMatrix(x, xp):
    n = x.shape[0]
    res = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            res[i, j] = xp[i, j] - x[i]
    return np.diag(np.random.random(n))


def gMatrix(f, x0, h):
    n = len(f)
    res = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            x = np.zeros(n)
            for k in range(n):
                x[k] = x0[k]
            x[j] += h[i, i]
            res[i, j] = f[i](x) - f[i](x0)
    return res


def nSolve(f, it):
    n = len(f)
    x = np.zeros(n)
    for i in range(it):
        addp = additionalPoints(x)
        h = hMatrix(x, addp)
        g = gMatrix(f, x, h)
        fdk = np.linalg.inv(g).dot(h)
        fk = np.array([f[j](x) for j in range(n)])
        x -= fdk.dot(fk)
        print(np.linalg.norm(fk))
        if np.linalg.norm(fk) < 10E-12:
            print('Точность достигнута')
            print('Количество итераций: ', i)
            break
    return x


f1 = [(lambda x: np.cos(x[0]) + 2*x[1]),
      (lambda x: x[0]*x[1] ** 2 - 10 * x[0] + 2)]

f2 = [(lambda x: x[1] ** 1.2 - np.sqrt(x[0] * 10 + 2) + 0.1),
      (lambda x: 3 - x[0] ** 1.7 + np.exp(-x[1] / 10 + 2))]

print(nSolve(f1, 20))
print(nSolve(f2, 20))


