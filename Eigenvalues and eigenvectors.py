import numpy as np

A = np.array([[2, 1], [1, 2]])

values, vectors = np.linalg.eig(A)

print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)

v = vectors[:, 0]
lam = values[0]

print("Av:", A @ v)
print("Lambda v:", lam * v)
