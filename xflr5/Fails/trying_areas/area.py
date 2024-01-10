import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

# Generate z values from 0 to 6
z_values = np.linspace(0, 6, 1000)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot all (x, y) values for each z value
for z in z_values:
    ax.plot(x_values, y_values, z, marker='o')

# Set plot title and labels
ax.set_title('3D Plot of Points with Varying Z-values')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()

# Your data points
