import numpy as np

eps = 10E-8


def lin_solve(a: np.array, f: np.array, it=1000):
    n = a.shape[0]
    x = np.zeros(n)
    for i in range(it):
        r = f - a.dot(x)
        ar = a.dot(r)
        al = ar.dot(r) / (ar.dot(ar))
        x += r * al
        if abs(np.linalg.norm(r)) < eps:
            print('Нужная точность была достигнута')
            print('Кол-во итераций: ', i)
            break
    return x


for _ in range(10):
    a = np.random.uniform(-12, 12, (5, 5))
    a = a.dot(a.transpose())
    f = np.random.uniform(-12, 12, a.shape[0])
    x = lin_solve(a, f)
    print(np.linalg.norm(a.dot(x) - f))

# a = np.array([[ 179.85765398,   28.38824355,  121.60049223,  202.20875581, -115.76418412],
#  [  28.38824355,  279.07925061,  159.36091406,  147.02509653,  -40.77474735],
#  [ 121.60049223,  159.36091406,  237.58868074,  191.04870008,  -67.73638304],
#  [ 202.20875581,  147.02509653,  191.04870008,  319.09346064, -172.50482382],
#  [-115.76418412,  -40.77474735,  -67.73638304, -172.50482382,  105.98049069]])
# f = np.array([ 5.01804507,  7.821133,    0.26578148,  2.65045199, 10.88873659])
# x = lin_solve(a, f)
# print(np.linalg.norm(a.dot(x) - f))
