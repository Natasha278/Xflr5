import matplotlib.pyplot as plt
import numpy as np
import math
import timeit

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
print('K list finished')

# lift coefficient optimus
cd0 = np.arange(0.05, 5, 0.05)
lift_coeff = np.sqrt(np.divide.outer(cd0, k)).flatten()
print('lift coeff list finished')

# Create a dictionary to store cl and corresponding cd0
cl_cd0_dict = {round(math.sqrt(cd0_val / k_val), 3): round(cd0_val, 3) for cd0_val in cd0 for k_val in k}
print('cl_cd0_dict finished')

# induced drag coefficient
idc = [round(k_val * (cl_val**2), 3) for k_val in k for cl_val in lift_coeff]
print('idc list finished')

# drag coefficient
cd = [round(i + idc_val, 2) for i in np.arange(0.05, 5, 0.5) for idc_val in idc]
print('cd list finished')

# Create a dictionary to store cl and corresponding cd1
cl_cd1_dict = {cl: rounded_cd1_val for cd1_val, k_val, rounded_cd1_val, cl in zip(cd, k, [round(cd1_val, 2) for cd1_val in cd], [round(math.sqrt(rounded_cd1_val / k_val), 3) for rounded_cd1_val, k_val in zip(cd, k)]) if cl_cd0_dict.get(cl) is not None}
print('cl_cd dict finished')

# efficiency
# efficiency
# eff = np.divide.outer(lift_coeff, idc).flatten()
# eff = np.round(eff, 3)
# print('eff list finished')
# eff = [round(cl_val / icd_val, 3) for icd_val in idc for cl_val in lift_coeff]
# print('eff list finished')
# efficiency
i = 0

eff = []
for icd_val in idc:
    i+=1
    if i%100 ==0:
        print(i)
    eff.extend([round(cl_val / icd_val, 3) for cl_val in lift_coeff])
eff = np.array(eff)
print('eff list finished')

# Lift at a height of 700m = 2296 ft and ISA + 0 
l = [0.5*1.145*(10**2)*a*lift_coeff_val for lift_coeff_val in lift_coeff]
print('l list finished')


# Measure the execution time
execution_time = timeit.timeit(lambda: None, number=1)

print(f"Execution time: {execution_time} seconds")