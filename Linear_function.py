import matplotlib.pyplot as plt

# Define the slope (m) and y-intercept (b) of the linear function
 
m = float(input('enter a value for the slope: '))  # Slope
b = float(input('enter a value for the intercept: ')) #intercept
    

# Generate x values (e.g., from -10 to 10)
x_values = range(-10, 11)

# Calculate y values using the linear function y = mx + b
y_values = [m*x + b for x in x_values]

# Plot the linear function
plt.plot(x_values, y_values, label=f'y = {m}x + {b}')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Function')
plt.grid(True)

# Add legend
plt.legend()

# Show the plot
plt.show()
