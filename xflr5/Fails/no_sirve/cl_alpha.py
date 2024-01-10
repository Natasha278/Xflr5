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

#Graph Cl vs Alpha
plt.figure()

for cl_val in lift_coeff:
    plt.scatter(alpha, [cl_val] * len(alpha), label=f'C$_l$ = {cl_val}')

# Ajustar los límites del eje y y x
plt.ylim(0, 13)
plt.xlim(3.5, 6.5)

# Etiquetas y título
plt.xlabel(chr(945))
plt.title('Angle of attack for each Lift coefficient value')
plt.ylabel('C$_l$')

# Añadir leyenda
max_cl_val = max(lift_coeff)
max_cl_idx = lift_coeff.index(max_cl_val)
plt.text(5, max_cl_val + 1.5, f'Max C$_l$ = {max_cl_val}', ha='center')
# Mostrar la gráfica
plt.show()
