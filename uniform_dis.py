import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Define parameters of the uniform distribution
a, b = 2, 10  # Lower and upper bounds
uniform_dist = stats.uniform(loc=a, scale=b-a)

# Calculate probability: P(4 ≤ X ≤ 8)
probability = uniform_dist.cdf(8) - uniform_dist.cdf(4)
print(f"Probability that X is between 4 and 8: {probability:.4f}")

# Generate values for plotting
x = np.linspace(a - 2, b + 2, 1000)
pdf_values = uniform_dist.pdf(x)
cdf_values = uniform_dist.cdf(x)

# Plot the PDF
plt.figure(figsize=(8, 4))
plt.plot(x, pdf_values, label="PDF", color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.fill_between(x, pdf_values, alpha=0.3, color='blue')
plt.title("Uniform Distribution PDF")
plt.xlabel("X")
plt.ylabel("Density")
plt.legend()
plt.grid()
plt.show()

# Plot the CDF
plt.figure(figsize=(8, 4))
plt.plot(x, cdf_values, label="CDF", color='red')
plt.axhline(0, color='black', linewidth=0.5)
plt.title("Uniform Distribution CDF")
plt.xlabel("X")
plt.ylabel("Cumulative Probability")
plt.legend()
plt.grid()
plt.show()
