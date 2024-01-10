import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import numpy as np

# Your data points
points = [
    (1.00003, 0.00126),
    (0.99730, 0.00170),
    (0.98914, 0.00302),
    (0.97563, 0.00518),
    (0.95693, 0.00812),
    (0.93324, 0.01176),
    (0.90482, 0.01602),
    (0.87197, 0.02079),
    (0.83506, 0.02597),
    (0.79449, 0.03145),
    (0.75070, 0.03712),
    (0.70417, 0.04285),
    (0.65541, 0.04854),
    (0.60496, 0.05405),
    (0.55335, 0.05924),
    (0.50117, 0.06397),
    (0.44897, 0.06811),
    (0.39733, 0.07150),
    (0.34681, 0.07402),
    (0.29796, 0.07554),
    (0.25131, 0.07597),
    (0.20738, 0.07524),
    (0.16604, 0.07320),
    (0.12732, 0.06915),
    (0.09230, 0.06265),
    (0.06203, 0.05382),
    (0.03730, 0.04324),
    (0.01865, 0.03176),
    (0.00628, 0.02030),
    (0.00015, 0.00956),
    (0.00000, 0.00000),
    (0.00533, -0.00792),
    (0.01557, -0.01401),
    (0.03029, -0.01870),
    (0.04915, -0.02248),
    (0.07195, -0.02586),
    (0.09868, -0.02922),
    (0.12954, -0.03282),
    (0.16483, -0.03660),
    (0.20483, -0.04016),
    (0.24869, -0.04283),
    (0.29531, -0.04446),
    (0.34418, -0.04510),
    (0.39476, -0.04482),
    (0.44650, -0.04371),
    (0.49883, -0.04188),
    (0.55117, -0.03945),
    (0.60296, -0.03655),
    (0.65360, -0.03327),
    (0.70257, -0.02975),
    (0.74930, -0.02607),
    (0.79330, -0.02235),
    (0.83407, -0.01866),
    (0.87118, -0.01512),
    (0.90420, -0.01180),
    (0.93279, -0.00880),
    (0.95661, -0.00621),
    (0.97543, -0.00410),
    (0.98901, -0.00254),
    (0.99722, -0.00158),
    (0.99997, -0.00126)
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