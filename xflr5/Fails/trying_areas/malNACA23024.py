import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import numpy as np

# Your data points
points = [
    (1.00000,	0.00000),
    (0.95036,	0.01724),
    (0.90064,	0.03115),
    (0.80116,	0.05687),
    (0.70162,	0.07988),
    (0.60202,	0.10008),
    (0.50235,	0.11690),
    (0.40256,	0.12928),
    (0.30265,	0.13546),
    (0.25262,	0.13535),
    (0.20253,	0.13237),
    (0.15001,	0.12528),
    (0.09423,	0.11049),
    (0.06601,	0.09844),
    (0.03853,	0.08172),
    (0.01331,	0.05764),
    (0.00277,	0.04017),
    (0.00000,	0.00000),
    (0.02223,	-0.03303),
    (0.03669,	-0.04432),
    (0.06147,	-0.05862),
    (0.08399,	-0.06860),
    (0.10577,	-0.07647),
    (0.14999,	-0.08852),
    (0.19747,	-0.09703),
    (0.24738,	-0.10223),
    (0.29735,	-0.10454),
    (0.39744,	-0.10278),
    (0.49766,	-0.09482),
    (0.59798,	-0.08242),
    (0.69838,	-0.06664),
    (0.79884,	-0.04803),
    (0.89936,	-0.02673),
    (0.94964,	-0.01504),
    (1.00000,	0.00000)
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

def calculate_area1(points1):
    sum = 0
    for i in range(len(points1)-1):
         sum += sqrt((points1[i][0] - points1[i + 1][0])**2 + (points1[i][1] - points1[i + 1][1])**2)
    area = sum * 75
    return area

def calculate_area2(points2):
    sum = 0
    for i in range(len(points2)-1):
         sum += sqrt((points2[i][0] - points2[i + 1][0])**2 + (points2[i][1] - points2[i+1][1])**2)
    area = sum * 75
    return area

# Your data points
points1 = [
    (1.00000*12.5,	0.00000),
    (0.95036*12.5,	0.01724),
    (0.90064*12.5,	0.03115),
    (0.80116*12.5,	0.05687),
    (0.70162*12.5,	0.07988),
    (0.60202*12.5,	0.10008),
    (0.50235*12.5,	0.11690),
    (0.40256*12.5,	0.12928),
    (0.30265*12.5,	0.13546),
    (0.25262*12.5,	0.13535),
    (0.20253*12.5,	0.13237),
    (0.15001*12.5,	0.12528),
    (0.09423*12.5,	0.11049),
    (0.06601*12.5,	0.09844),
    (0.03853*12.5,	0.08172),
    (0.01331*12.5,	0.05764),
    (0.00277*12.5,	0.04017),
    (0.00000,	0.00000)]

points2=[
    (0.02223*12.5,	-0.03303),
    (0.03669*12.5,	-0.04432),
    (0.06147*12.5,	-0.05862),
    (0.08399*12.5,	-0.06860),
    (0.10577*12.5,	-0.07647),
    (0.14999*12.5,	-0.08852),
    (0.19747*12.5,	-0.09703),
    (0.24738*12.5,	-0.10223),
    (0.29735*12.5,	-0.10454),
    (0.39744*12.5,	-0.10278),
    (0.49766*12.5,	-0.09482),
    (0.59798*12.5,	-0.08242),
    (0.69838*12.5,	-0.06664),
    (0.79884*12.5,	-0.04803),
    (0.89936*12.5,	-0.02673),
    (0.94964*12.5,	-0.01504),
    (1.00000*12.5,	0.00000)
]

# Calculate area
area1 = calculate_area1(points1)
area2 = calculate_area2(points2)
print("Area of the closed figure:", area1 + area2)
