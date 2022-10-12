import numpy as np

eps = 10E-8


def iter_solve(a: np.array, f: np.array, it=100):
    n = a.shape[0]
    x = np.zeros(n)
    r = f - a.dot(x)
    s = r * 1
    for i in range(it):
        alpha = r.dot(r) / (a.dot(s)).dot(s)
        x += alpha * s
        old_r = np.array(r)
        r -= alpha * a.dot(s)
        betta = (r.dot(r)) / (old_r.dot(old_r))
        s = r + betta * s
        if abs(np.linalg.norm(r)) < eps:
            print('Нужная точность была достигнута')
            print('Кол-во итераций: ', i)
            break
    return x


def test():
    a = np.array(np.random.uniform(-12, 12, (5, 5)))
    a = a.dot(a.transpose())
    f = np.array(np.random.uniform(-12, 12, 5))
    x = iter_solve(a, f)
    print(np.linalg.norm(a.dot(x) - f))
    f1 = np.matrix(f)
    f1.resize((5, 1))
    x1 = np.matrix(x)
    x1.resize((5, 1))
    print(a)
    print(f1)
    print(x1)
    res = np.matrix(a.dot(x))
    res.resize((5, 1))
    print(res)



test()

