import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math

# Given values
span = 1.5
chord = 0.2

# Aspect Ratio
a_r = span / chord

# Oswald efficiency number
#changed 0.05 to 0.01
osw_eff = np.arange(0.05, 1, 0.01).round(3).tolist()

k = []
for n in osw_eff:
    k1 = round(1 / (math.pi * n * a_r), 3)
    k.append(k1)

# lift coefficient optimus
lift_coeff = []
#changed 0.5 to 0.05
cd0 = list(np.arange(0.05, 5, 0.05, dtype=float))

for cd0_val in cd0:  # specify dtype=float
    for k_val in k:
        cl = round(math.sqrt(cd0_val / k_val), 3)
        lift_coeff.append(cl)

# Reshape the lift_coeff array to a 2D array for plotting
lift_coeff_2d = np.array(lift_coeff).reshape(len(cd0), len(k))

# Plotting
for i, cd0_val in enumerate(cd0):
    plt.plot(osw_eff, lift_coeff_2d[i, :], label=f'CD0 = {cd0_val}')

plt.xlabel('Oswald Efficiency Number')
plt.ylabel('Lift Coefficient')
plt.title('Lift Coefficient vs. Oswald Efficiency Number for Different CD0')
plt.legend()
plt.show()



"""
To create a graph that represents the relationship between the lists of values (k, cd0, lift_coeff), we can use a 3D plot since you have three variables. However, since we are interested in the maximum value of lift_coeff, it might be more informative to create 2D plots for different values of cd0.
This code creates a 2D plot with the Oswald Efficiency Number on the x-axis, Lift Coefficient on the y-axis, and different lines representing different values of CD0. It can be can visualize how the Lift Coefficient changes for various CD0 values.
"""
