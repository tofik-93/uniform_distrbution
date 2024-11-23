import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from scipy.stats import expon
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_exponential_pdf():
    try:
        scale_param = float(scale_param_entry.get())
        num_samples = int(num_samples_entry.get())

        # Generate random samples from the exponential distribution
        samples = np.random.exponential(scale_param, num_samples)

        # Calculate PDF
        x = np.linspace(0, max(samples) * 2, 1000)
        pdf = expon.pdf(x, scale=scale_param)

        # Plot histogram
        ax[0].clear()
        ax[0].hist(samples, bins=30, density=True, alpha=0.6, color='g')
        ax[0].set_title('Histogram')
        ax[0].set_xlabel('Value')
        ax[0].set_ylabel('Frequency')

        # Plot PDF
        ax[1].clear()
        ax[1].plot(x, pdf, label='PDF')
        ax[1].set_title('Exponential Distribution PDF')
        ax[1].set_xlabel('Value')
        ax[1].set_ylabel('Probability Density')
        ax[1].legend()
        ax[1].grid(True)

        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter valid input values.")

# Create main window
root = tk.Tk()
root.title("Exponential Distribution PDF Plotter")

# Create a frame for input fields
input_frame = ttk.Frame(root, padding="20")
input_frame.grid(row=0, column=0, padx=10, pady=10)

# Scale parameter input
scale_param_label = ttk.Label(input_frame, text="Scale Parameter:")
scale_param_label.grid(row=0, column=0, sticky="w", pady=5)
scale_param_entry = ttk.Entry(input_frame)
scale_param_entry.grid(row=0, column=1, sticky="w", pady=5)

# Number of samples input
num_samples_label = ttk.Label(input_frame, text="Number of Samples:")
num_samples_label.grid(row=1, column=0, sticky="w", pady=5)
num_samples_entry = ttk.Entry(input_frame)
num_samples_entry.grid(row=1, column=1, sticky="w", pady=5)

# Plot button
plot_button = ttk.Button(input_frame, text="Plot PDF", command=plot_exponential_pdf)
plot_button.grid(row=2, columnspan=2, pady=10)

# Create a frame for the plot
plot_frame = ttk.Frame(root)
plot_frame.grid(row=1, column=0)

# Create matplotlib figure and canvas
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()
