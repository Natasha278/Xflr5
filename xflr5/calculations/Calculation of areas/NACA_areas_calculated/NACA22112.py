import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

# Your data points
points = [
    (1.000009, 0.00126),
    (0.999324, 0.001361),
    (0.997273, 0.001663),
    (0.99386, 0.002165),
    (0.989095, 0.002863),
    (0.982991, 0.003753),
    (0.975566, 0.004829),
    (0.966839, 0.006085),
    (0.956836, 0.007513),
    (0.945583, 0.009104),
    (0.933112, 0.010851),
    (0.919458, 0.012742),
    (0.904657, 0.014769),
    (0.888752, 0.01692),
    (0.871785, 0.019184),
    (0.853803, 0.02155),
    (0.834856, 0.024007),
    (0.814996, 0.026542),
    (0.794277, 0.029144),
    (0.772756, 0.0318),
    (0.750491, 0.034496),
    (0.727545, 0.03722),
    (0.703978, 0.039957),
    (0.679857, 0.042693),
    (0.655245, 0.045413),
    (0.630212, 0.048101),
    (0.604823, 0.050741),
    (0.57915, 0.053316),
    (0.553261, 0.055807),
    (0.527227, 0.058198),
    (0.501118, 0.060468),
    (0.475006, 0.0626),
    (0.448962, 0.064575),
    (0.423056, 0.066374),
    (0.39736, 0.067978),
    (0.371941, 0.06937),
    (0.346871, 0.070534),
    (0.322217, 0.071454),
    (0.298047, 0.072116),
    (0.274426, 0.072508),
    (0.251419, 0.072621),
    (0.229089, 0.072445),
    (0.207497, 0.071975),
    (0.186702, 0.071209),
    (0.166762, 0.070146),
    (0.147731, 0.068787),
    (0.129656, 0.067136),
    (0.112144, 0.065149),
    (0.095138, 0.062628),
    (0.078921, 0.059413),
    (0.063758, 0.055436),
    (0.049888, 0.050716),
    (0.037508, 0.04535),
    (0.02677, 0.039497),
    (0.017766, 0.033349),
    (0.010541, 0.027108),
    (0.005093, 0.020965),
    (0.001383, 0.015082),
    (-0.000647, 0.009583),
    (-0.001078, 0.004546),
    (0.0, 0.0),
    (0.002449, -0.003975),
    (0.006126, -0.007341),
    (0.010928, -0.010182),
    (0.01676, -0.012605),
    (0.023533, -0.014729),
    (0.031177, -0.016671),
    (0.03965, -0.018543),
    (0.048946, -0.020441),
    (0.059106, -0.022439),
    (0.070217, -0.024594),
    (0.082409, -0.026937),
    (0.095845, -0.029467),
    (0.11071, -0.032136),
    (0.127199, -0.034826),
    (0.145162, -0.037349),
    (0.164108, -0.039627),
    (0.183978, -0.041652),
    (0.204718, -0.043419),
    (0.226272, -0.044926),
    (0.248581, -0.04617),
    (0.271584, -0.047154),
    (0.295217, -0.04788),
    (0.319415, -0.048354),
    (0.344112, -0.048583),
    (0.36924, -0.048576),
    (0.394729, -0.048342),
    (0.420509, -0.047894),
    (0.446509, -0.047244),
    (0.472658, -0.046404),
    (0.498882, -0.045389),
    (0.525109, -0.044212),
    (0.551268, -0.042888),
    (0.577285, -0.041432),
    (0.603088, -0.039857),
    (0.628607, -0.038178),
    (0.653772, -0.036408),
    (0.678511, -0.034563),
    (0.702758, -0.032654),
    (0.726446, -0.030696),
    (0.749509, -0.028703),
    (0.771883, -0.026686),
    (0.793508, -0.024661),
    (0.814325, -0.022639),
    (0.834275, -0.020635),
    (0.853304, -0.018661),
    (0.87136, -0.016732),
    (0.888394, -0.014859),
    (0.90436, -0.013058),
    (0.919213, -0.011341),
    (0.932913, -0.009721),
    (0.945423, -0.008211),
    (0.95671, -0.006822),
    (0.966741, -0.005567),
    (0.975491, -0.004456),
    (0.982935, -0.003498),
    (0.989053, -0.002702),
    (0.993828, -0.002076),
    (0.997249, -0.001624),
    (0.999305, -0.001351),
    (0.999991, -0.00126)
]
# Separate x and y coordinates
x_values, y_values = zip(*points)

# Find the maximum x value
max_x = max(x_values)

# Calculate the factor to transform the maximum x to 12.5
factor = 12.5 / max_x

# Multiply all x and y values by the calculated factor
x_values = [x * factor for x in x_values]
y_values = [y * factor for y in y_values]

modified_points = [(x, y) for x, y in zip(x_values, y_values)]

# Generate more z values for smoother representation
z_values = np.linspace(0, 6, 10000)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
ax = fig.add_subplot(111, projection='3d')

# Plot all (x, y) values for each z value
for z in z_values:
    ax.plot(x_values, y_values, z, marker='', linestyle='-')

# Set plot title and labels
ax.set_title('3D Plot of Points with Varying Z-values')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set x-axis ticks and grid in increments of 0.01
x_ticks = np.arange(0, 12.51, 0.5)
ax.set_xticks(x_ticks)
ax.set_xticklabels(["{:.2f}".format(tick) for tick in x_ticks], rotation=45)

# Set y-axis ticks and grid to match x-axis
y_ticks = np.arange(min(y_values), max(y_values) + 0.01, 0.01)
ax.set_yticks(y_ticks)
ax.set_yticklabels(["{:.2f}".format(tick) for tick in y_ticks], rotation=45)

# Ensure equal aspect ratio
ax.set_box_aspect([np.ptp(arr) for arr in [x_values, y_values, z_values]])

# Show the plot
plt.show()


def calculate_area(modified_points):
    sum = 0
    for i in range(len(modified_points)-1):
         sum += sqrt((modified_points[i][0] - modified_points[i + 1][0])**2 + (modified_points[i][1] - modified_points[i+1][1])**2)
    area = sum * 150
    return area

# Calculate area
area = calculate_area(modified_points)
print("Area of the closed figure:", area)

#Calculus of thickness
max_y = max(y_values)*factor
min_y = min(y_values)*factor
thickness = max_y-min_y
print(thickness)

