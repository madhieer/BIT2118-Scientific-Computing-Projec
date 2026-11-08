import numpy as np

np.random.seed(42)

simulations = 100000

returns = np.random.normal(
    loc=0.08,
    scale=0.15,
    size=simulations
)

probability_loss = np.mean(returns < 0)

print("Average return:", np.mean(returns))
print("Probability of loss:", probability_loss)

# Change volatility
returns2 = np.random.normal(0.08, 0.25, simulations)

print("New probability of loss:",
      np.mean(returns2 < 0))
