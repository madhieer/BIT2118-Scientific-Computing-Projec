import numpy as np

readings = np.array([25.5, 26.0, 27.2, 24.8, 26.5])

print("Readings:", readings)
print("Mean:", np.mean(readings))
print("Maximum:", np.max(readings))
print("Minimum:", np.min(readings))

# Change one reading
readings[2] = 30.0
print("New mean:", np.mean(readings))
