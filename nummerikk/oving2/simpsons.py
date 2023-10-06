import numpy as np


def integrerSimpsons(f, a, b, n):
    dx = (b-a)/n

    area = f(a) + f(b)
    for i in range(1, n):
        area += (2 if i % 2 == 0 else 4)*f(a+i*dx)

    return dx/3*area


def f(x, k):
    return k+x*x


a = 0
b = 3
n = 2
k = 2

print(integrerSimpsons(lambda x: f(x, k), a, b, n))
