import numpy as np

A = np.array([[2, 3], [4, 5]])
B = np.array([[1, 2], [3, 4]])

print("Addition:\n", A + B)
print("Multiplication:\n", A @ B)
print("Transpose:\n", A.T)
print("Determinant:", np.linalg.det(A))
