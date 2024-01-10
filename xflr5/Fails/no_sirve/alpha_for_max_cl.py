# import matplotlib.pyplot as plt
# import numpy as np
# import math

# # Given parameters
# span = 1.5
# chord = 0.2
# a_r = span / chord
# osw_eff = np.arange(0.05, 1, 0.05).round(3).tolist()

# # Calculate k values
# k = [round(1 / (math.pi * n * a_r), 3) for n in osw_eff]

# # Calculate lift coefficients for different alpha values
# lift_coeff = []
# cd0 = list(np.arange(0.05, 5, 0.5, dtype=float))
# alpha_vals = list(np.arange(4, 6.1, 0.5, dtype=float))

# for alpha_val in alpha_vals:
#     for cd0_val, k_val in zip(cd0, k):
#         cl = round(math.sqrt(cd0_val / k_val) * alpha_val, 3)
#         lift_coeff.append(cl)

# # Reshape the lift_coeff array for plotting
# lift_coeff = np.array(lift_coeff).reshape(len(cd0), len(osw_eff))

# # Transpose the lift_coeff array
# lift_coeff = lift_coeff.T

# # Plotting
# fig, ax = plt.subplots(figsize=(10, 6))
# c = ax.contourf(osw_eff, cd0, lift_coeff, cmap='viridis')
# plt.colorbar(c, label='Lift Coefficient')

# ax.set_xlabel('Oswald Efficiency Factor')
# ax.set_ylabel('CD0 (Zero-lift Drag Coefficient)')
# ax.set_title('Lift Coefficient vs. Oswald Efficiency and CD0')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import math

# Given parameters
span = 1.5
chord = 0.2
a_r = span / chord
osw_eff = np.arange(0.05, 1, 0.05).round(3).tolist()

# Calculate k values
k = [round(1 / (math.pi * n * a_r), 3) for n in osw_eff]

# Calculate lift coefficients for different alpha values
lift_coeff = []
cd0 = list(np.arange(0.05, 5, 0.5, dtype=float))
alpha_vals = list(np.arange(4, 6.1, 0.5, dtype=float))

for cd0_val in cd0:
    for alpha_val, k_val in zip(alpha_vals, k):
        cl = round(math.sqrt(cd0_val / k_val) * alpha_val, 3)
        lift_coeff.append(cl)

# Check if the size of lift_coeff matches the expected size
expected_size = len(osw_eff) * len(alpha_vals)
if len(lift_coeff) != expected_size:
    raise ValueError(f"Size mismatch: {len(lift_coeff)} != {expected_size}")

# Reshape the lift_coeff array for plotting
lift_coeff = np.array(lift_coeff).reshape(len(osw_eff), len(alpha_vals))

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
c = ax.contourf(alpha_vals, osw_eff, lift_coeff, cmap='viridis')
plt.colorbar(c, label='Lift Coefficient')

ax.set_xlabel('Angle of Attack')
ax.set_ylabel('Oswald Efficiency Factor')
ax.set_title('Lift Coefficient vs. Angle of Attack and Oswald Efficiency')
plt.show()



