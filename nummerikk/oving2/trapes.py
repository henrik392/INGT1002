import numpy as np

def integrerTrapes(f, a, b, n):
    result = 0
    dx = (b-a)/n
    for i in range(n):
        result += (f(a+dx*i) + f(a+dx*(i+1)))*dx/2

    return result


def f(x):
    return 4*x*x


def f_d(x):
    return 8*x


def kurvelengde_d(f_d):
    return lambda x: np.sqrt(1+f_d(x)**2)

a = -1/2
b = 2
n = 100

print(integrerTrapes(kurvelengde_d(f_d), a, b, n))