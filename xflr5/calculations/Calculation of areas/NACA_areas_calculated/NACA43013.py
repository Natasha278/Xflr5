import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import numpy as np

# Your data points
points = [
    (1.000060, 0.001364),
    (0.998529, 0.001666),
    (0.993946, 0.002567),
    (0.986337, 0.004054),
    (0.975750, 0.006105),
    (0.962249, 0.008692),
    (0.945917, 0.011777),
    (0.926853, 0.015321),
    (0.905174, 0.019277),
    (0.881012, 0.023597),
    (0.854515, 0.028230),
    (0.825845, 0.033123),
    (0.795179, 0.038222),
    (0.762704, 0.043472),
    (0.728619, 0.048815),
    (0.693133, 0.054192),
    (0.656464, 0.059544),
    (0.618837, 0.064805),
    (0.580482, 0.069911),
    (0.541634, 0.074792),
    (0.502531, 0.079380),
    (0.463411, 0.083602),
    (0.424515, 0.087389),
    (0.386079, 0.090671),
    (0.348339, 0.093385),
    (0.311526, 0.095472),
    (0.275866, 0.096882),
    (0.241575, 0.097577),
    (0.208866, 0.097527),
    (0.177227, 0.096639),
    (0.146103, 0.094269),
    (0.116295, 0.089762),
    (0.088645, 0.082847),
    (0.063946, 0.073663),
    (0.042832, 0.062714),
    (0.025704, 0.050738),
    (0.012716, 0.038544),
    (0.003833, 0.026879),
    (-0.001098, 0.016339),
    (-0.002293, 0.007320),
    (0.000000, 0.000000),
    (0.005375, -0.005455),
    (0.013409, -0.009069),
    (0.023797, -0.011225),
    (0.036228, -0.012394),
    (0.050416, -0.013066),
    (0.066161, -0.013681),
    (0.083414, -0.014577),
    (0.102338, -0.015982),
    (0.123299, -0.018027),
    (0.146790, -0.020743),
    (0.173325, -0.024001),
    (0.203349, -0.027398),
    (0.235926, -0.030331),
    (0.270144, -0.032663),
    (0.305790, -0.034402),
    (0.342644, -0.035568),
    (0.380476, -0.036192),
    (0.419051, -0.036312),
    (0.458130, -0.035969),
    (0.497469, -0.035212),
    (0.536825, -0.034090),
    (0.575952, -0.032652),
    (0.614608, -0.030948),
    (0.652553, -0.029024),
    (0.689550, -0.026927),
    (0.725372, -0.024699),
    (0.759795, -0.022382),
    (0.792607, -0.020016),
    (0.823603, -0.017640),
    (0.852592, -0.015293),
    (0.879394, -0.013015),
    (0.903843, -0.010842),
    (0.925787, -0.008812),
    (0.945089, -0.006963),
    (0.961630, -0.005330),
    (0.975306, -0.003944),
    (0.986033, -0.002834),
    (0.993743, -0.002023),
    (0.998388, -0.001529),
    (0.999940, -0.001364)
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