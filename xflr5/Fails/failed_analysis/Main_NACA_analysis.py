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

k = []
for n in osw_eff:
    k1 = round(1 / (math.pi * n * a_r), 3)
    k.append(k1)

print('K list finished')

# lift coefficient optimus
lift_coeff = []
cd0 = list(np.arange(0.05, 5, 0.05, dtype=float))

print('lift coeff list finished')

# Create a dictionary to store cl and corresponding cd0
cl_cd0_dict = {}

for cd0_val in cd0:  # specify dtype=float
    rounded_cd0_val = round(cd0_val, 3)
    for k_val in k:
        cl = round(math.sqrt(rounded_cd0_val / k_val), 3)
        lift_coeff.append(cl)

        # Store cl and corresponding cd0 in the dictionary
        cl_cd0_dict[cl] = rounded_cd0_val

print('cl_cd0_dict finished')



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

print('max cl_cd0_dict list finished')

# induced drag coefficient
idc = []
for k_val in k:
    for cl_val in lift_coeff:
        idc1 = round(k_val * (cl_val**2), 3)
        idc.append(idc1)

print('idc list finished')

# drag coefficient
cd = []
for i in np.arange(0.05, 5, 0.5, dtype=float):  # specify dtype=float
    for idc_val in idc:
        cd1 = round(i + idc_val, 2)
        cd.append(cd1)

print('cd list finished')

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

print('cl_cd dict finished')


# efficiency
eff = []
print(len(idc))
print(len(lift_coeff))
for icd_val in idc:
    print('1 more done')
    for cl_val in lift_coeff:
        eff1 = round(cl_val / icd_val, 3)
        eff.append(eff1)

print('eff list finished')

#Lift at a hight of 700m = 2296 ft and ISA + 0 
l = []
for lift_coeff_val in lift_coeff:
    lift = 0.5*1.145*(10**2)*a*lift_coeff_val
    l.append(lift)

print('l list finished')