import numpy as np
import matplotlib.pyplot as plt

# Generate data for the main graph
x_main = np.linspace(0, 10, 100)
y_main = np.sin(x_main)

# Generate data for the inset graph
x_inset = np.linspace(7, 8, 50)
y_inset = np.sin(x_inset)

# Create the main figure and axes
fig, ax = plt.subplots()

# Plot the main graph
ax.plot(x_main, y_main, label='Main Graph')

# Create the inset axes
inset_ax = ax.inset_axes([0.7, 0.3, 0.2, 0.2])  # Specify the position and size of the inset axes

# Plot the inset graph
inset_ax.plot(x_inset, y_inset, label='Inset Graph')

# Customize the inset axes
inset_ax.set_xlabel('X Inset')
inset_ax.set_ylabel('Y Inset')

# Customize the inset marker and line style
inset_ax.plot(x_inset, y_inset, marker='o', linestyle='--', color='r')

# Add a legend to the main graph
ax.legend()

# Add a title to the main graph
ax.set_title('Main Graph with Inset')

# Display the plot
plt.show()
