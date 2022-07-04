import numpy as np

h = 10E-6


def get_h(n):
    res = np.zeros([n, n])
    for i in range(n):
        res[i, i] = h
    return res


def get_g(f, x0):
    n = len(f)
    res = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            x = np.zeros(n)
            for k in range(n):
                x[k] = x0[k]
            x[j] += h
            res[i, j] = f[i](x) - f[i](x0)
    return res


def nsolve(f, it):
    n = len(f)
    x = np.zeros(n)
    hm = get_h(n)
    for i in range(it):
        g = get_g(f, x)
        fdk = np.linalg.inv(g).dot(hm)
        fk = np.zeros(n)
        for j in range(n):
            fk[j] = f[j](x)
        x -= fdk.dot(fk)
        if np.linalg.norm(fk)<10E-12:
            print('Нужная точность была достигнута')
            print('Кол-во итераций: ', i)
            break
    return x


f1 = [(lambda x: np.sin(x[0]) + x[1]),
      (lambda x: x[1] ** 2 - 10 * x[0] + 2)]

f2 = [(lambda x: x[1]**1.2-np.sqrt(x[0]*10+2)+0.1),
      (lambda x: 3-x[0] ** 1.7 + np.exp(-x[1]/10+2))]

print(nsolve(f1, 10))
print()
print(nsolve(f2, 10))
