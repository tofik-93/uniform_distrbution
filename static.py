import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error

# 1️⃣ Generating a dataset
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=1000)  # Normal Distribution

# 2️⃣ Descriptive Statistics
mean_val = np.mean(data)
variance_val = np.var(data)
std_dev_val = np.std(data)
print(f"Mean: {mean_val}, Variance: {variance_val}, Std Dev: {std_dev_val}")

# 3️⃣ Probability Distributions
x = np.linspace(20, 80, 1000)
pdf = stats.norm.pdf(x, loc=mean_val, scale=std_dev_val)
plt.plot(x, pdf, label="Normal Distribution")
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.legend()
plt.title("Normal Distribution of Data")
plt.show()

# 4️⃣ Naïve Bayes (Using a synthetic dataset)
X = np.random.rand(100, 2)  # Features
y = np.random.choice([0, 1], size=100)  # Binary labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
y_pred = nb_model.predict(X_test)
print(f"Naïve Bayes Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# 5️⃣ Linear Regression (Predicting numerical values)
X_reg = np.random.rand(100, 1) * 10  # Feature
y_reg = 2.5 * X_reg + np.random.randn(100, 1) * 2  # Target with noise

X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_reg = lr_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred_reg)
print(f"Linear Regression MSE: {mse:.2f}")

# Plotting Linear Regression
plt.scatter(X_test, y_test, color="blue", label="Actual Data")
plt.plot(X_test, y_pred_reg, color="red", label="Predicted Line")
plt.legend()
plt.title("Linear Regression")
plt.show()
