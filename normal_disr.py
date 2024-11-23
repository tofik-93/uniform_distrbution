import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_pdf():
    try:
        mean = float(mean_entry.get())
        std_dev = float(std_dev_entry.get())

        x = np.linspace(-5*std_dev + mean, 5*std_dev + mean, 1000)
        pdf = norm.pdf(x, mean, std_dev)

        ax.clear()
        ax.plot(x, pdf, label='PDF')
        ax.set_title('Normal Distribution PDF')
        ax.set_xlabel('Value')
        ax.set_ylabel('Probability Density')
        ax.legend()
        ax.grid(True)
        canvas.draw()
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter valid input values.")

# Create main window
root = tk.Tk()
root.title("Normal Distribution PDF Plotter")

# Create a frame for input fields
input_frame = ttk.Frame(root, padding="20")
input_frame.grid(row=0, column=0)

# Mean input
mean_label = ttk.Label(input_frame, text="Mean:")
mean_label.grid(row=0, column=0, sticky="w", pady=5)
mean_entry = ttk.Entry(input_frame)
mean_entry.grid(row=0, column=1, sticky="w", pady=5)

# Standard deviation input
std_dev_label = ttk.Label(input_frame, text="Standard Deviation:")
std_dev_label.grid(row=1, column=0, sticky="w", pady=5)
std_dev_entry = ttk.Entry(input_frame)
std_dev_entry.grid(row=1, column=1, sticky="w", pady=5)

# Plot button
plot_button = ttk.Button(input_frame, text="Plot PDF", command=plot_pdf)
plot_button.grid(row=2, columnspan=2, pady=10)

# Create a frame for the plot
plot_frame = ttk.Frame(root)
plot_frame.grid(row=1, column=0)

# Create matplotlib figure and canvas
fig, ax = plt.subplots(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()
