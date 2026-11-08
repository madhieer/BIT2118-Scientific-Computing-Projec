import numpy as np
from scipy.integrate import trapezoid

time = np.array([0, 1, 2, 3, 4])
power = np.array([2, 3, 4, 3, 2])

energy = trapezoid(power, time)

print("Energy consumed:", energy, "kWh")

# Increase power consumption by 20%
new_energy = trapezoid(power * 1.2, time)
print("New energy:", new_energy, "kWh")
