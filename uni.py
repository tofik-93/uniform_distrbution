import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Parameters
low = 0     # Lower bound
high = 10   # Upper bound
size = 1000  # Number of samples

# Generate uniform distribution
data = uniform.rvs(loc=low, scale=high-low, size=size)

# Plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')

# Plot theoretical PDF
x = np.linspace(low, high, 1000)
plt.plot(x, uniform.pdf(x, loc=low, scale=high-low), 'r-', lw=2)

plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
