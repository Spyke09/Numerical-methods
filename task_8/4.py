import numpy as np

eps = 10E-8


def qr_gram_schmidt(a1: np.matrix):
    a = a1 * 1
    n = a.shape[0]
    r = np.zeros(a.shape)
    q = r * 1

    for k in range(n):
        s = 0
        for j in range(n):
            s += a[j, k] ** 2
            r[k, k] = np.sqrt(s)
        for j in range(n):
            q[j, k] = a[j, k] / r[k, k]
        for i in range(k, n):
            s = 0
            for j in range(n):
                s += a[j, i] * q[j, k]
                r[k, i] = s
            for j in range(n):
                a[j, i] = a[j, i] - r[k, i] * q[j, k]
    return np.asmatrix(q), np.asmatrix(r)


def qr_alg(a1, iter=100):
    a = a1 * 1
    res = a
    t = 0
    id = np.identity(a.shape[0])
    for i in range(iter):
        q, r = qr_gram_schmidt(a - t * id)
        a = r * q + t * id
        t = a[-1 , -1]
        if abs(np.linalg.norm(a.diagonal() - res.diagonal())) < eps:
            print('Нужная точность была достигнута')
            print('Кол-во итераций: ', i + 1)
            break
        res = a
    return a.diagonal()


def test():
    a = np.array(np.random.uniform(-3, 3, (5, 5)))
    a = a.dot(a.transpose())
    print(np.linalg.eigvals(a))
    qr_alg(a, 200)


test()
