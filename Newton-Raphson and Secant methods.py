def f(x):
    return x**2 - 49

def df(x):
    return 2*x

x = 10

for i in range(10):
    x = x - f(x)/df(x)

print("Newton-Raphson root:", x)

# Secant method
x0, x1 = 5.0, 10.0

for i in range(10):
    x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    x0, x1 = x1, x2

print("Secant root:", x1)
