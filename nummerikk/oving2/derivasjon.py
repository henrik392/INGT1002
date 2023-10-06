
def derivert(f, x, h):
    return (f(x+h)-f(x))/h

def senter_diff(f, x, h):
    return (f(x+h/2)-f(x-h/2))/h


def f(x):
    return (x-2)**2+1


h = 0.1
x = 1

print(derivert(f, x, h))
print(senter_diff(f, x, h))
