population = 1000
rate = 0.05
h = 1

for year in range(5):
    population = population + h * rate * population
    print(year + 1, population)
