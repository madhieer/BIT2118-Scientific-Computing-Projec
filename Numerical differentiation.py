import numpy as np

time = np.array([0, 1, 2, 3, 4])
position = np.array([0, 5, 12, 21, 32])

velocity = np.gradient(position, time)

print("Velocity:", velocity)

# Change position data
position = position * 2
print("New velocity:", np.gradient(position, time))
