import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math

#span, chord, k, e, a
#a_r

NACA_foils = []

#NACA foil area
a = 54

span = 1.5
chord = 0.2


# Aspect Ratio 
a_r = span / chord

# Oswald efficiency number
osw_eff = np.arange(0.05, 1, 0.05).round(3).tolist()

k = []
for n in osw_eff:
    k1 = round(1 / (math.pi * n * a_r), 3)
    k.append(k1)

# lift coefficient optimus
lift_coeff = []
cd0 = list(np.arange(0.05, 5, 0.5, dtype=float))

for cd0_val in cd0:  # specify dtype=float
  for k_val in k:
      cl = round(math.sqrt(cd0_val / k_val), 3)
      lift_coeff.append(cl)

#induced drag coefficient
idc = []
for k_val in k:
  for cl_val in lift_coeff:
      idc1 = round(k_val*(cl_val**2), 3)
      idc.append(idc1)


#drag coefficient
cd = []
for i in np.arange(0.05, 5, 0.5, dtype=float):  # specify dtype=float
    for idc_val in idc:
        cd1 = round(i + idc_val, 2)
        cd.append(cd1)

# efficiency
eff = []
for icd_val in idc:
    for cl_val in lift_coeff:
        eff1 = round(cl_val / icd_val, 3)
        eff.append(eff1)

#Lift at a hight of 700m = 2296 ft and ISA + 0 
l = []
for lift_coeff_val in lift_coeff:
    lift = 0.5*1.145*(10**2)*a*lift_coeff_val
    l.append(lift)


alpha = list(np.arange(4, 6.1, 0.5, dtype=float))



#k optimus graph
plt.figure()

plt.scatter(osw_eff, k, label=f'k = {k_val}', c='black')

# Ajustar los límites del eje y y x
plt.ylim(0, 1.1)
plt.xlim(0, 1.1)

# Etiquetas y título
plt.xlabel('Parasitic drag coefficient')
plt.title('cl optimus')
plt.ylabel('cl')

# Añadir leyenda
max_e_val = max(osw_eff)
max_e_idx = osw_eff.index(max_e_val)
plt.text(0.55, max_e_val + 0.03, f'Max e = {max_e_val}', ha='center')
min_k_val = min(k)
min_k_idx = k.index(min_k_val)
plt.text(0.55, min_k_val + 0.85, f'Min k = {min_k_val}', ha='center')
# Mostrar la gráfica
plt.show()