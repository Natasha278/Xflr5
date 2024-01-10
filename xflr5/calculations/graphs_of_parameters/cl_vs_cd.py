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

# induced drag coefficient
idc = []
for k_val in k:
    for cl_val in lift_coeff:
        idc1 = round(k_val * (cl_val**2), 3)
        idc.append(idc1)

# drag coefficient
cd = []
for i in np.arange(0.05, 5, 0.5, dtype=float):  # specify dtype=float
    for idc_val in idc:
        cd1 = round(i + idc_val, 2)
        cd.append(cd1)

# Create a dictionary to store cl and corresponding cd1
cl_cd1_dict = {}

for cd1_val, k_val in zip(cd, k):
    rounded_cd1_val = round(cd1_val, 2)

    # Obtener los valores de cl y cd0 correspondientes
    cl = round(math.sqrt(rounded_cd1_val / k_val), 3)
    cd0_val = cl_cd0_dict.get(cl, None)

    # Si el valor de cd0 no está en el diccionario, continuamos con la siguiente iteración
    if cd0_val is None:
        continue

    # Store cl and corresponding cd1 in the dictionary
    cl_cd1_dict[cl] = rounded_cd1_val

# Create lists for plotting
cl_values = list(cl_cd1_dict.keys())
cd1_values = list(cl_cd1_dict.values())

# Plotting
plt.plot(cl_values, cd1_values, label='cl vs. cd1')
plt.xlabel('cl (Lift Coefficient)')
plt.ylabel('cd1 (Drag Coefficient)')
plt.title('Relationship between cl and cd1')
plt.legend()
plt.grid(True)
plt.show()


"""
The size of the resulting dictionary (cl_cd1_dict) may be smaller than expected due to the way it's constructed in the provided code. The dictionary is built by iterating over the cd values and attempting to find the corresponding values of cl and cd0. However, the relationship between cd, cl, and cd0 is complex, and not every combination of cd values will have a corresponding cl and cd0 value in the dataset.
"""