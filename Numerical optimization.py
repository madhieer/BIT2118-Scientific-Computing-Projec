from scipy.optimize import minimize

def cost(x):
    quantity = x[0]
    return 2*quantity**2 - 40*quantity + 500

result = minimize(cost, [5])

print("Optimal quantity:", result.x)
print("Minimum cost:", result.fun)

# Compare with a different starting point
result2 = minimize(cost, [15])
print("Alternative solution:", result2.x)
