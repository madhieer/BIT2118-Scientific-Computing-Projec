import numpy as np
from scipy.interpolate import interp1d

time = np.array([1, 2, 4, 5])
temperature = np.array([20, 22, 26, 28])

model = interp1d(time, temperature)

print("Estimated temperature:", model(3))

# Change the measurement at time 4
temperature[2] = 30
model = interp1d(time, temperature)
print("New estimate:", model(3))
