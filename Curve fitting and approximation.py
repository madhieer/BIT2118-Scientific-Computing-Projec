import numpy as np
from scipy.optimize import curve_fit

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 14, 19, 25, 32])

def model(x, a, b):
    return a*x + b

parameters, _ = curve_fit(model, x, y)

print("Parameters:", parameters)
print("Prediction:", model(6, *parameters))
