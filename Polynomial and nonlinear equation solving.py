import numpy as np

coefficients = [1, -5, 6]

roots = np.roots(coefficients)

print("Polynomial roots:", roots)

# Change the constant term
new_roots = np.roots([1, -5, 4])
print("Modified roots:", new_roots)
