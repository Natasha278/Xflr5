import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import numpy as np

# Your data points
points = [
    (1.000006, 0.00126),
    (0.999322, 0.00136),
    (0.99727, 0.001658),
    (0.993856, 0.002153),
    (0.98909, 0.002843),
    (0.982986, 0.003723),
    (0.97556, 0.004789),
    (0.966834, 0.006035),
    (0.956831, 0.007455),
    (0.945581, 0.009042),
    (0.933114, 0.010787),
    (0.919464, 0.012683),
    (0.904671, 0.014721),
    (0.888775, 0.016891),
    (0.871819, 0.019184),
    (0.853852, 0.021589),
    (0.834921, 0.024096),
    (0.81508, 0.026695),
    (0.794383, 0.029373),
    (0.772886, 0.032119),
    (0.750648, 0.03492),
    (0.72773, 0.037763),
    (0.704194, 0.040634),
    (0.680104, 0.043518),
    (0.655525, 0.046401),
    (0.630525, 0.049266),
    (0.60517, 0.052095),
    (0.57953, 0.05487),
    (0.553674, 0.057574),
    (0.527671, 0.060186),
    (0.501592, 0.062686),
    (0.475508, 0.065055),
    (0.449488, 0.067272),
    (0.423604, 0.069316),
    (0.397925, 0.071169),
    (0.372521, 0.07281),
    (0.347461, 0.074221),
    (0.322813, 0.075386),
    (0.298645, 0.076289),
    (0.275022, 0.076917),
    (0.252008, 0.077258),
    (0.229667, 0.077304),
    (0.208021, 0.077046),
    (0.186846, 0.076424),
    (0.166208, 0.07531),
    (0.146246, 0.073603),
    (0.127102, 0.071238),
    (0.108917, 0.068189),
    (0.091825, 0.064466),
    (0.075952, 0.060115),
    (0.061409, 0.055211),
    (0.048288, 0.049855),
    (0.036662, 0.044161),
    (0.026586, 0.038255),
    (0.018089, 0.032261),
    (0.011185, 0.026299),
    (0.005872, 0.020474),
    (0.002131, 0.014875),
    (-6.8e-05, 0.009571),
    (-0.000762, 0.004606),
    (0.0, 0.0),
    (0.002133, -0.004151),
    (0.005546, -0.007772),
    (0.010181, -0.010904),
    (0.01598, -0.013598),
    (0.022889, -0.015916),
    (0.030855, -0.017927),
    (0.039834, -0.019703),
    (0.049792, -0.021313),
    (0.060706, -0.022825),
    (0.072566, -0.0243),
    (0.085377, -0.02579),
    (0.099158, -0.027339),
    (0.113937, -0.028977),
    (0.129753, -0.030719),
    (0.146647, -0.032563),
    (0.164661, -0.034483),
    (0.183833, -0.03643),
    (0.204194, -0.038319),
    (0.225694, -0.040034),
    (0.247992, -0.041499),
    (0.270988, -0.042711),
    (0.294618, -0.043673),
    (0.318819, -0.044389),
    (0.343522, -0.044863),
    (0.36866, -0.045104),
    (0.394163, -0.045121),
    (0.419962, -0.044922),
    (0.445983, -0.044519),
    (0.472156, -0.043923),
    (0.498408, -0.043146),
    (0.524665, -0.042202),
    (0.550855, -0.041102),
    (0.576904, -0.039859),
    (0.602741, -0.038488),
    (0.628294, -0.037),
    (0.653492, -0.035408),
    (0.678264, -0.033727),
    (0.702543, -0.031969),
    (0.726261, -0.030146),
    (0.749352, -0.028273),
    (0.771753, -0.026363),
    (0.793402, -0.024429),
    (0.81424, -0.022484),
    (0.834209, -0.020544),
    (0.853255, -0.018621),
    (0.871326, -0.016731),
    (0.888371, -0.014888),
    (0.904346, -0.013106),
    (0.919206, -0.0114),
    (0.932912, -0.009784),
    (0.945426, -0.008273),
    (0.956714, -0.00688),
    (0.966747, -0.005617),
    (0.975496, -0.004496),
    (0.98294, -0.003528),
    (0.989057, -0.002723),
    (0.993832, -0.002088),
    (0.997252, -0.001629),
    (0.999308, -0.001353),
    (0.999994, -0.00126)
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