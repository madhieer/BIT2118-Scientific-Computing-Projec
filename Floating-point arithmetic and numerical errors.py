a = 0.1 + 0.2
b = 0.3

print(a)
print(b)
print("Exact equality:", a == b)

import numpy as np
print("Tolerance comparison:", np.isclose(a, b))

# Change the tolerance
print(np.isclose(a, b, atol=1e-12))
