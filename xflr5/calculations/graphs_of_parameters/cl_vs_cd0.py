import matplotlib.pyplot as plt
import numpy as np
import math

# span, chord, k, e, a
# a_r

NACA_foils = []

# NACA foil area
a = 54

span = 1.5
chord = 0.2

# Aspect Ratio
a_r = span / chord

# Oswald efficiency number
osw_eff = np.arange(0.05, 1, 0.01).round(3).tolist()

k = []
for n in osw_eff:
    k1 = round(1 / (math.pi * n * a_r), 3)
    k.append(k1)

# lift coefficient optimus
lift_coeff = []
cd0 = list(np.arange(0.05, 5, 0.05, dtype=float))

# Create a dictionary to store cl and corresponding cd0
cl_cd0_dict = {}

for cd0_val in cd0:  # specify dtype=float
    rounded_cd0_val = round(cd0_val, 3)
    for k_val in k:
        cl = round(math.sqrt(rounded_cd0_val / k_val), 3)
        lift_coeff.append(cl)

        # Store cl and corresponding cd0 in the dictionary
        cl_cd0_dict[cl] = rounded_cd0_val

# Create lists for plotting
cl_values = list(cl_cd0_dict.keys())
cd0_values = list(cl_cd0_dict.values())

# Perform polynomial regression (fit a trendline)
degree = 2  # You can adjust the degree of the polynomial
coefficients = np.polyfit(cd0_values, cl_values, degree)
poly_function = np.poly1d(coefficients)

# Plot both graphs in subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plot the first graph with the trendline
axs[0].plot(cd0_values, cl_values, marker='o', linestyle='-', color='b', label='Data Points')
axs[0].plot(cd0_values, poly_function(cd0_values), linestyle='--', color='r', label=f'Trendline (degree={degree})')
axs[0].set_title('Relationship between cd0 and cl with Trendline')
axs[0].set_xlabel('cd0')
axs[0].set_ylabel('cl')
axs[0].legend()
axs[0].grid(True)

# Create a dictionary to store max cl and corresponding cd0
cl_cd0_dict = {}

for cd0_val in cd0:  # specify dtype=float
    rounded_cd0_val = round(cd0_val, 3)
    max_cl = -1  # Initialize max_cl for each cd0
    for k_val in k:
        cl = round(math.sqrt(rounded_cd0_val / k_val), 3)
        if cl > max_cl:
            max_cl = cl

        # Store cl and corresponding cd0 in the dictionary
        cl_cd0_dict[rounded_cd0_val] = max_cl

# Create lists for plotting
cd0_values = list(cl_cd0_dict.keys())
max_cl_values = list(cl_cd0_dict.values())

# Plot the second graph with the maxima line
axs[1].plot(cd0_values, max_cl_values, marker='o', linestyle='-', color='b', label='Maximum CL for each CD0')
axs[1].set_title('Maximum CL for each CD0')
axs[1].set_xlabel('CD0')
axs[1].set_ylabel('Maximum CL')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
