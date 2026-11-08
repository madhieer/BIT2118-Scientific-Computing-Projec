import numpy as np

A = np.array([[4., 1.], [1., 3.]])
b = np.array([9., 7.])

x = np.zeros(2)

for i in range(100):
    old = x.copy()
    x[0] = (9 - old[1]) / 4
    x[1] = (7 - old[0]) / 3

print("Approximate solution:", x)
print("Residual:", b - A @ x)
