# import numpy as np
# import matplotlib.pyplot as plt
# values = np.random.uniform(0.01, 0.99, 1000)

# count, bins, ignored = plt.hist(values, 20, density=True)
# plt.plot(bins, np.ones_like(bins),color='r')
# plt.title('Uniform Distribution')
# plt.ylabel('Density')
# plt.xlabel('values')
# plt.show()

from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np

x = uniform.rvs(0.01,0.99, size=1000)
print(f'pdf of x is {uniform.pdf(x[0])}')

plt.hist(x, density = True)
plt.axhline(y=uniform.pdf(x[0]),color='r')
plt.title('uniform distribution')
plt.ylabel('Density')
plt.xlabel('X')
plt.show()