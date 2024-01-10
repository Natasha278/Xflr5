import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import numpy as np

# Your data points
points = [
    (1.0000, 0.0022),
    (0.9500, 0.0153),
    (0.9000, 0.0276),
    (0.8000, 0.0505),
    (0.7000, 0.0709),
    (0.6000, 0.0890),
    (0.5000, 0.1040),
    (0.4000, 0.1149),
    (0.3000, 0.1206),
    (0.2500, 0.1205),
    (0.2000, 0.1180),
    (0.1500, 0.1119),
    (0.1000, 0.1003),
    (0.0750, 0.0913),
    (0.0500, 0.0793),
    (0.0250, 0.0641),
    (0.0125, 0.0487),
    (0.0000, 0.0000),
    (0.0125, -0.0208),
    (0.0250, -0.0314),
    (0.0500, -0.0452),
    (0.0750, -0.0555),
    (0.1000, -0.0632),
    (0.1500, -0.0751),
    (0.2000, -0.0830),
    (0.2500, -0.0876),
    (0.3000, -0.0895),
    (0.4000, -0.0883),
    (0.5000, -0.0814),
    (0.6000, -0.0707),
    (0.7000, -0.0572),
    (0.8000, -0.0413),
    (0.9000, -0.0230),
    (0.9500, -0.0130),
    (1.0000, -0.0022) 
]

# Separate x and y coordinates
x_values, y_values = zip(*points)

# Find the maximum x value
max_x = max(x_values)

# Calculate the factor to transform the maximum x to 12.5
factor = 12.5 / max_x

# # Multiply all x and y values by the calculated factor
# x_values = [x * factor for x in x_values]
# y_values = [y * factor for y in y_values]

# modified_points = [(x, y) for x, y in zip(x_values, y_values)]

# # Generate more z values for smoother representation
# z_values = np.linspace(0, 6, 10000)

# # Create a 3D plot
# fig = plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
# ax = fig.add_subplot(111, projection='3d')

# # Plot all (x, y) values for each z value
# for z in z_values:
#     ax.plot(x_values, y_values, z, marker='', linestyle='-')

# # Set plot title and labels
# ax.set_title('3D Plot of Points with Varying Z-values')
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')

# # Set x-axis ticks and grid in increments of 0.01
# x_ticks = np.arange(0, 12.51, 0.5)
# ax.set_xticks(x_ticks)
# ax.set_xticklabels(["{:.2f}".format(tick) for tick in x_ticks], rotation=45)

# # Set y-axis ticks and grid to match x-axis
# y_ticks = np.arange(min(y_values), max(y_values) + 0.01, 0.01)
# ax.set_yticks(y_ticks)
# ax.set_yticklabels(["{:.2f}".format(tick) for tick in y_ticks], rotation=45)

# # Ensure equal aspect ratio
# ax.set_box_aspect([np.ptp(arr) for arr in [x_values, y_values, z_values]])

# # Show the plot
# plt.show()


# def calculate_area(modified_points):
#     sum = 0
#     for i in range(len(modified_points)-1):
#          sum += sqrt((modified_points[i][0] - modified_points[i + 1][0])**2 + (modified_points[i][1] - modified_points[i + 1][1])**2)
#     area = sum * 150
#     return area

# # Calculate area
# area = calculate_area(modified_points)
# print("Area of the closed figure:", area)

#Calculus of thickness
max_y = max(y_values)*factor
min_y = min(y_values)*factor
thickness = max_y-min_y
print(thickness)