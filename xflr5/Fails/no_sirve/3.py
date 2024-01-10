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

# Plot the graph with the trendline
plt.plot(cd0_values, cl_values, marker='o', linestyle='-', color='b', label='Data Points')
plt.plot(cd0_values, poly_function(cd0_values), linestyle='--', color='r', label=f'Trendline (degree={degree})')
plt.title('Relationship between cd0 and cl with Trendline')
plt.xlabel('cd0')
plt.ylabel('cl')
plt.legend()
plt.grid(True)
plt.show()


