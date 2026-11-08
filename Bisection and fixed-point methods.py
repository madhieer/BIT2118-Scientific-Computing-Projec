def f(x):
    return x**2 - 25

a, b = 0, 10

for i in range(30):
    mid = (a + b) / 2

    if f(a) * f(mid) < 0:
        b = mid
    else:
        a = mid

print("Root:", mid)

# Fixed-point method
x = 3.0
for i in range(20):
    x = (x + 25/x) / 2

print("Fixed point:", x)
