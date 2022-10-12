class Polynomial:
    def __init__(self, coef):
        self.__coef = coef

    def __len__(self):
        return len(self.__coef)

    def __call__(self, x):
        t = 1
        answer = 0
        for i in reversed(self.__coef):
            answer += t * i
            t *= x

    def __getitem__(self, idx):
        return self.__coef[idx]

    def __setitem__(self, idx, value):
        self.__coef[idx] = value

    def __divmod__(self, other):
        a = self.__coef.copy()
        n1 = len(self)
        n2 = len(other)
        div, mod = [], []
        c = 0
        while n1 >= n2 + c:
            k = a[c] / other[0]
            for i in range(len(other)):
                a[i + c] -= other[i] * k
            div.append(k)
            c += 1
        for i in range(c, len(a)):
            mod.append(a[i])
        return Polynomial(div), Polynomial(mod)

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Polynomial([i / other for i in self.__coef])
        return divmod(self, other)[0]

    def __mod__(self, other):
        return divmod(self, other)[1]

    def __repr__(self):
        r = []
        n = len(self) - 1
        for i in self.__coef:
            c = f"{round(i, 3)}x^{n}" if i >= 0 else f"({round(i, 3)})x^{n}"
            r.append(c)
            n -= 1
        return (" + ".join(r))[:-3]

    def __mul__(self, other):
        a, b = self.__coef, other.__coef
        l = len(a) + len(b) - 1
        c = [0 for i in range(l)]
        for i in range(len(a)):
            for j in range(len(b)):
                c[i + j] += a[i] * b[j]
        return Polynomial(c)


def bairstow_method_one(p: Polynomial, it=100):
    u, v = 0, 0
    a = Polynomial([1, u, v])
    for _ in range(it):
        q, mod_p = divmod(p, a)
        r, mod_q = divmod(q, a)
        c, d = mod_p[0], mod_p[1]
        g, h = mod_q[0], mod_q[1] if len(mod_q) > 1 else 0
        if (v * g ** 2 + h * (h - u * g)) == 0:
            return p
        de = -1 / (v * g ** 2 + h * (h - u * g))
        u += de * (-h * c + g * d)
        v += de * (-g * v * c + (g * u - h) * d)
        a = Polynomial([1, u, v])
    return a


def bairstow_method(a):
    q = []
    while len(a) > 2:
        p = bairstow_method_one(a)
        q.append(p)
        a = a / p
    q.append(a)
    return q


a = Polynomial([1, 4, 10, -14, 8, 0, 1])
res = bairstow_method(a)
b = Polynomial([1])
for i in res:
    b = b * i
print(b)
