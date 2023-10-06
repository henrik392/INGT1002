from fractions import Fraction

a = 0
b = 1

n = 4

dx = (b-a)/n

def f(x):
    return (3 + x*x)

A = 0

for i in range(4):
    A += (f(i*dx)+f((i+1)*dx))/2*dx

print(Fraction(A))