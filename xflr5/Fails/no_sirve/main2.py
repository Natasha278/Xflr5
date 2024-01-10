import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math

# span, chord, k, e, a
# a_r

NACA_foils = []

# NACA foil area
a = 54

# Given values
span = 1.5
chord = 0.2
alpha = list(np.arange(4, 6.1, 0.5, dtype=float))

# Aspect Ratio
a_r = span / chord

# Oswald efficiency number
osw_eff = np.arange(0.05, 1, 0.01).round(3).tolist()

# Calculate K values
k = [round(1 / (math.pi * n * a_r), 3) for n in osw_eff]
print('K list finished')

# lift coefficient optimus
cd0 = list(np.arange(0.05, 5, 0.05, dtype=float))
lift_coeff = [round(math.sqrt(cd0_val / k_val), 3) for cd0_val in cd0 for k_val in k]
print('lift coeff list finished')

# Create a dictionary to store cl and corresponding cd0
cl_cd0_dict = {cl: round(cd0_val, 3) for cl, cd0_val in zip(lift_coeff, cd0)}
print('cl_cd0_dict finished')

# Create a dictionary to store max cl and corresponding cd0
cl_cd0_dict = {}
for cd0_val in cd0:
    rounded_cd0_val = round(cd0_val, 3)
    max_cl = -1
    for k_val in k:
        cl = round(math.sqrt(rounded_cd0_val / k_val), 3)
        if cl > max_cl:
            max_cl = cl
    cl_cd0_dict[rounded_cd0_val] = max_cl
print('max cl_cd0_dict list finished')

# induced drag coefficient
idc = [round(k_val * (cl_val**2), 3) for k_val in k for cl_val in lift_coeff]
print('idc list finished')

# drag coefficient
cd = [round(i + idc_val, 2) for i in np.arange(0.05, 5, 0.5, dtype=float) for idc_val in idc]
print('cd list finished')

# Create a dictionary to store cl and corresponding cd1
cl_cd1_dict = {}
for cd1_val, k_val in zip(cd, k):
    rounded_cd1_val = round(cd1_val, 2)
    cl = round(math.sqrt(rounded_cd1_val / k_val), 3)
    cd0_val = cl_cd0_dict.get(cl, None)
    if cd0_val is None:
        continue
    cl_cd1_dict[cl] = rounded_cd1_val
print('cl_cd dict finished')

# efficiency
eff = [round(cl_val / icd_val, 3) for icd_val in idc for cl_val in lift_coeff]
print('eff list finished')

# Lift at a height of 700m = 2296 ft and ISA + 0 
l = [0.5*1.145*(10**2)*a*lift_coeff_val for lift_coeff_val in lift_coeff]
print('l list finished')



"""
import matplotlib.pyplot as plt
import numpy as np
import math

# span, chord, k, e, a
# a_r

NACA_foils = []

# NACA foil area
a = 54

# Given values
span = 1.5
chord = 0.2
alpha = np.arange(4, 6.1, 0.5, dtype=float)

# Aspect Ratio
a_r = span / chord

# Oswald efficiency number
osw_eff = np.arange(0.05, 1, 0.01).round(3)

# Calculate K values
k = np.round(1 / (math.pi * osw_eff * a_r), 3)
print('K list finished')

# lift coefficient optimus
cd0 = np.arange(0.05, 5, 0.05, dtype=float)
lift_coeff = np.round(np.sqrt(np.outer(cd0, 1 / k)), 3)
print('lift coeff list finished')

# Create a dictionary to store cl and corresponding cd0
cl_cd0_dict = {cl: round(cd0_val, 3) for cl, cd0_val in zip(lift_coeff.flatten(), cd0)}
print('cl_cd0_dict finished')

# Create a dictionary to store max cl and corresponding cd0
cl_cd0_dict = {}
for cd0_val in cd0:
    rounded_cd0_val = round(cd0_val, 3)
    max_cl = np.max(np.sqrt(rounded_cd0_val / k))
    cl_cd0_dict[rounded_cd0_val] = round(max_cl, 3)
print('max cl_cd0_dict list finished')

# induced drag coefficient
idc = np.round(k * np.square(lift_coeff), 3)
print('idc list finished')

# drag coefficient
cd = np.round(np.outer(np.arange(0.05, 5, 0.5), 1) + idc, 2)
print('cd list finished')

# Create a dictionary to store cl and corresponding cd1
cl_cd1_dict = {}
for cd1_val, k_val in zip(cd.flatten(), k):
    rounded_cd1_val = round(cd1_val, 2)
    cl = round(np.sqrt(rounded_cd1_val / k_val), 3)
    cd0_val = cl_cd0_dict.get(cl, None)
    if cd0_val is None:
        continue
    cl_cd1_dict[cl] = rounded_cd1_val
print('cl_cd dict finished')

# efficiency
eff = np.round(np.divide(lift_coeff.flatten(), idc), 3)
print('eff list finished')

# Lift at a height of 700m = 2296 ft and ISA + 0 
l = 0.5 * 1.145 * (10 ** 2) * a * lift_coeff.flatten()
print('l list finished')
"""