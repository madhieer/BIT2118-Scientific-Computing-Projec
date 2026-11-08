import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def cooling(t, T):
    return -0.1 * (T - 25)

times = np.linspace(0, 20, 100)

result = solve_ivp(
    cooling, (0, 20), [90],
    t_eval=times
)

plt.plot(result.t, result.y[0])
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Cooling Process")
plt.grid()
plt.show()

print("Final temperature:", result.y[0][-1])
