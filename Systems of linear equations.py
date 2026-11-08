import numpy as np

A = np.array([[2, 1], [1, 3]])
b = np.array([100, 120])

solution = np.linalg.solve(A, b)

print("Solution:", solution)
print("Verification:", A @ solution)
