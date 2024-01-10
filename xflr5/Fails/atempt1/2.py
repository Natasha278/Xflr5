import matplotlib.pyplot as plt
import numpy as np
import math

# Given values
span = 1.5
chord = 0.2

# Aspect Ratio
a_r = span / chord

# Oswald efficiency number
osw_eff = np.arange(0.05, 1, 0.05).round(3).tolist()

k = set()
for n in osw_eff:
    k1 = round(1 / (math.pi * n * a_r), 3)
    k.add(k1)

# lift coefficient optimus
lift_coeff = set()  # Cambiando de lista a conjunto

cd0 = list(np.arange(0.05, 5, 0.5, dtype=float))

for cd0_val in cd0:  # specify dtype=float
    for k_val in k:
        cl = round(math.sqrt(cd0_val / k_val), 3)
        lift_coeff.add(cl)  # Cambiando de append a add

# Verificando el tamaño del conjunto
expected_size = len(cd0) * len(k)
lift_coeff_list = list(lift_coeff)
assert len(lift_coeff_list) == expected_size, f"Error: Tamaño incorrecto del conjunto lift_coeff. Se esperaba {expected_size}, pero se obtuvo {len(lift_coeff_list)}"

# Reshape the lift_coeff array to a 2D array for plotting
lift_coeff_2d = np.array(lift_coeff_list).reshape(len(cd0), len(k))

# Plotting
for i, cd0_val in enumerate(cd0):
    plt.plot(osw_eff, lift_coeff_2d[i, :], label=f'CD0 = {cd0_val}')

plt.xlabel('Oswald Efficiency Number')
plt.ylabel('Lift Coefficient')
plt.title('Lift Coefficient vs. Oswald Efficiency Number for Different CD0')
plt.legend()
plt.show()
