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
alpha = [round(x, 1) for x in np.arange(4, 6.1, 0.5)]

# Aspect Ratio
a_r = span / chord

# Oswald efficiency number
osw_eff = [round(x, 3) for x in np.arange(0.05, 1, 0.01)]

# Calculate K values
k = np.array([round(1 / (math.pi * n * a_r), 3) for n in osw_eff])

# lift coefficient optimus
cd0 = np.arange(0.05, 5, 0.05)
lift_coeff = np.sqrt(np.divide.outer(cd0, k)).flatten()

# Create a dictionary to store cl and corresponding cd0
cl_cd0_dict = {round(math.sqrt(cd0_val / k_val), 3): round(cd0_val, 3) for cd0_val in cd0 for k_val in k}

# induced drag coefficient
idc = [round(k_val * (cl_val**2), 3) for k_val in k for cl_val in lift_coeff]

# drag coefficient
cd = [round(cd0_val + idc_val, 2) for cd0_val in cd0 for idc_val in idc]

# Create a dictionary to store cl and corresponding cd1
cl_cd1_dict = {cl: rounded_cd1_val for cd1_val, k_val, rounded_cd1_val, cl in zip(cd, k, [round(cd1_val, 2) for cd1_val in cd], [round(math.sqrt(rounded_cd1_val / k_val), 3) for rounded_cd1_val, k_val in zip(cd, k)]) if cl_cd0_dict.get(cl) is not None}

eff = []
for cd_val in cd:
    eff.extend([round(cl_val / cd_val, 3) for cl_val in lift_coeff])
eff = np.array(eff)

# Lift at a height of 700m = 2296 ft and ISA + 0 
l = [0.5*1.145*(10**2)*a*lift_coeff_val for lift_coeff_val in lift_coeff]

#create a dictionary to store all the values of eff with its respectively value of cl, cd, l, d, e, k, etc.