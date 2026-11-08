import numpy as np
from scipy.linalg import lu

A = np.array([[4., 2.], [8., 12.]])
b = np.array([20., 72.])

P, L, U = lu(A)

print("Permutation:\n", P)
print("Lower triangular:\n", L)
print("Upper triangular:\n", U)

x = np.linalg.solve(A, b)
print("Solution:", x)
