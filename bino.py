import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 10     # Number of trials
p = 0.5    # Probability of success
size = 1000  # Number of samples

# Generate binomial distribution data
data = np.random.binomial(n, p, size)

# Plot histogram
plt.hist(data, bins=np.arange(0, n+2) - 0.5, density=True, alpha=0.6, color='b', edgecolor='black')

# Plot theoretical PMF
x = np.arange(0, n+1)
plt.plot(x, binom.pmf(x, n, p), 'ro', ms=8, label='binom pmf')

plt.title('Binomial Distribution')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.xticks(x)
plt.legend()
plt.show()
