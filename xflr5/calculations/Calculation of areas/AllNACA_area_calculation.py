import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
import ast


#Create a file for each NACA
name = input("Insert NACA type: ")


# Data points of the specific NACA airfoil
points_string = input("Insert points: ")

# Evaluate the input string
points = [ast.literal_eval(points_string)]
thickness = float(input("Insert thickness: "))

# Flatten the list of tuples (points)
points = [item for sublist in points for item in sublist]

# Separate x and y coordinates to operate with them
x_values, y_values = zip(*points)

# Find the maximum x value
max_x = max(x_values)

# Calculate the factor to transform the maximum x to thickness
factor = thickness / max_x

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
ax.set_title(f'NACA{name}')
ax.set_xlabel(f'chord of {thickness} cm')
ax.set_ylabel(f'hight of {max(y_values)} cm')
ax.set_zlabel('lenght of 75 cm')

# Set x-axis ticks and grid in increments of 0.01
x_ticks = np.arange(0, thickness + 0.01, 0.5)
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
         sum += sqrt((modified_points[i][0] - modified_points[i + 1][0])**2 + (modified_points[i][1] - modified_points[i + 1][1])**2)
    area = sum * 150
    return area

# Calculate area
area = calculate_area(modified_points)
print("Area of the closed figure:", area)

#Calculus of thickness
max_y = max(y_values)
min_y = min(y_values)
thickness = max_y-min_y
print(thickness)


source_file_path = 'AllNACA.py'
destination_file_path = f'NACA{name}.py'

# Read the contents of the source file
with open(source_file_path, 'r') as source:
    source_code = source.readlines()

# Find the line number where the 'points' list is defined
points_line_number = source_code.index("points = [ast.literal_eval(points_string)]\n")
# Replace the 'points' list with the modified points
source_code[points_line_number] = "points = {}\n".format(modified_points)


# Find the line number where the 'name' is defined
name_line_number = source_code.index('name = input("Insert NACA type: ")\n')
# Replace the 'name' with the modified name
source_code[name_line_number] = f"name = '{name}'\n"


# Define the line numbers to exclude
line_ranges = [(85, 129), (11, 14), (18, 20)]  # replace with the actual line number ranges

# Remove the undesired lines
modified_source_code = [line for i, line in enumerate(source_code) if all(i < start - 1 or i >= end for start, end in line_ranges)]

# Convert the list back to a string and remove the undesired paragraph
modified_source_code_str = ''.join(modified_source_code)

# Write the modified content to the destination file
with open(destination_file_path, 'a') as destination:
    destination.write(modified_source_code_str)


#ones we analyze each NACA in xflr5:
                                #Make different graphs for each NACA
#calculate the thickness of the NACA by substracting the maximum y value from the minimum y value
    
#choose the correct thickness of a NACA with a specific length accoding to the rate taked.

#choose points until next x is smaller than actual x  

#calculate thickness
    