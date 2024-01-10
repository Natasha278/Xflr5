
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

# lift coefficient optimus
cd0 = np.arange(0.05, 5, 0.05)
lift_coeff = np.sqrt(np.divide.outer(cd0, k)).flatten()

# Create a dictionary to store cl and corresponding cd0
cl_cd0_dict = {round(math.sqrt(cd0_val / k_val), 3): round(cd0_val, 3) for cd0_val in cd0 for k_val in k}

# induced drag coefficient
idc = [round(k_val * (cl_val**2), 3) for k_val in k for cl_val in lift_coeff]

# drag coefficient
cd = [round(i + idc_val, 2) for i in np.arange(0.05, 5, 0.5) for idc_val in idc]

# Create a dictionary to store cl and corresponding cd1
cl_cd1_dict = {cl: rounded_cd1_val for cd1_val, k_val, rounded_cd1_val, cl in zip(cd, k, [round(cd1_val, 2) for cd1_val in cd], [round(math.sqrt(rounded_cd1_val / k_val), 3) for rounded_cd1_val, k_val in zip(cd, k)]) if cl_cd0_dict.get(cl) is not None}

# Obtener todos los valores de cl y cd1
cl_values = list(cl_cd1_dict.keys())
cd1_values = list(cl_cd1_dict.values())

# Calcular la eficiencia (eff) como cl/cd1 para cada valor de cl
eff = [cl / cd1 for cl, cd1 in zip(cl_values, cd1_values)]

# Crear una gráfica en función de cl
plt.scatter(cl_values, eff, marker='o', linestyle='-', color='p')
plt.xlabel('cl')
plt.ylabel('Eff [cl / cd]')
plt.title('Gráfica de eficiencia en función del lift coefficient')
plt.show()