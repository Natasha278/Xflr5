
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import numpy as np

# Your data points
points = [
    (0.999997, 0.00126),
    (0.999312, 0.001354),
    (0.997258, 0.001637),
    (0.993841, 0.002108),
    (0.989071, 0.002764),
    (0.982963, 0.003604),
    (0.975533, 0.004625),
    (0.966803, 0.005823),
    (0.956798, 0.007194),
    (0.945547, 0.008733),
    (0.933082, 0.010435),
    (0.919438, 0.012296),
    (0.904653, 0.014307),
    (0.888769, 0.016464),
    (0.87183, 0.018759),
    (0.853884, 0.021184),
    (0.83498, 0.023731),
    (0.815169, 0.026391),
    (0.794507, 0.029153),
    (0.773049, 0.032008),
    (0.750855, 0.034943),
    (0.727983, 0.037946),
    (0.704497, 0.041003),
    (0.680458, 0.044098),
    (0.655933, 0.047215),
    (0.630985, 0.050336),
    (0.605683, 0.053443),
    (0.580094, 0.056516),
    (0.554286, 0.059534),
    (0.528328, 0.062473),
    (0.50229, 0.065313),
    (0.47624, 0.068029),
    (0.45025, 0.070599),
    (0.424388, 0.072998),
    (0.398725, 0.075204),
    (0.373329, 0.077194),
    (0.34827, 0.078948),
    (0.323614, 0.080447),
    (0.299332, 0.081663),
    (0.275377, 0.082518),
    (0.251837, 0.08292),
    (0.228804, 0.082793),
    (0.206376, 0.082077),
    (0.184653, 0.080733),
    (0.163736, 0.078741),
    (0.143728, 0.076102),
    (0.124726, 0.072835),
    (0.106827, 0.06898),
    (0.090117, 0.064594),
    (0.074674, 0.059745),
    (0.060568, 0.054517),
    (0.047855, 0.048997),
    (0.036581, 0.043279),
    (0.026779, 0.037454),
    (0.018472, 0.031612),
    (0.01167, 0.025834),
    (0.006375, 0.020194),
    (0.002579, 0.014751),
    (0.000268, 0.009552),
    (-0.000583, 0.00463),
    (0.0, 0.0),
    (0.001953, -0.004237),
    (0.005211, -0.007994),
    (0.009732, -0.011291),
    (0.015477, -0.01416),
    (0.022404, -0.016637),
    (0.030472, -0.018765),
    (0.03964, -0.020591),
    (0.049873, -0.022162),
    (0.061138, -0.023529),
    (0.073407, -0.02474),
    (0.086655, -0.025841),
    (0.100866, -0.026875),
    (0.116027, -0.027879),
    (0.132129, -0.028888),
    (0.149166, -0.029925),
    (0.167133, -0.031011),
    (0.186027, -0.032153),
    (0.205839, -0.03335),
    (0.226557, -0.03459),
    (0.248163, -0.035848),
    (0.270632, -0.037084),
    (0.293931, -0.038245),
    (0.318018, -0.039264),
    (0.342713, -0.040071),
    (0.367852, -0.040656),
    (0.393363, -0.041023),
    (0.419177, -0.04118),
    (0.445221, -0.041134),
    (0.471424, -0.040894),
    (0.49771, -0.040468),
    (0.524008, -0.039867),
    (0.550242, -0.039099),
    (0.57634, -0.038175),
    (0.602228, -0.037105),
    (0.627834, -0.0359),
    (0.653084, -0.034571),
    (0.67791, -0.033128),
    (0.70224, -0.031584),
    (0.726007, -0.02995),
    (0.749145, -0.02824),
    (0.77159, -0.026466),
    (0.793278, -0.024643),
    (0.814151, -0.022785),
    (0.834151, -0.020907),
    (0.853223, -0.019025),
    (0.871314, -0.017155),
    (0.888377, -0.015314),
    (0.904364, -0.01352),
    (0.919233, -0.011788),
    (0.932943, -0.010137),
    (0.945459, -0.008583),
    (0.956747, -0.007142),
    (0.966777, -0.005829),
    (0.975524, -0.00466),
    (0.982963, -0.003647),
    (0.989076, -0.002801),
    (0.993847, -0.002133),
    (0.997264, -0.00165),
    (0.999318, -0.001358),
    (1.000003, -0.00126)
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