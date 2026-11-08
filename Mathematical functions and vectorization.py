import numpy as np
import time

units = np.arange(1, 1000001)
price = 25

cost = units * price

print("First five costs:", cost[:5])
print("Total cost:", np.sum(cost))
