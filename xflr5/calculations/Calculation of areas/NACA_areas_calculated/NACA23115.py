import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import numpy as np

# Your data points
points = [
    (0, 0),
    (0.00021186, 0.0036268),
    (0.00097385, 0.00736689),
    (0.00229789, 0.01121666),
    (0.00419462, 0.01516549),
    (0.00667325, 0.01919955),
    (0.00974134, 0.0233019),
    (0.01340461, 0.02745272),
    (0.01766665, 0.03162962),
    (0.02252878, 0.03580789),
    (0.02798967, 0.03996101),
    (0.03404525, 0.04406109),
    (0.04068839, 0.04807941),
    (0.04790881, 0.05198701),
    (0.05569297, 0.0557554),
    (0.06402403, 0.05935718),
    (0.07288189, 0.06276672),
    (0.08224337, 0.06596088),
    (0.0920824, 0.06891963),
    (0.1023703, 0.07162662),
    (0.1130763, 0.07406969),
    (0.1241677, 0.07624129),
    (0.1356105, 0.07813874),
    (0.147396, 0.07976448),
    (0.1594097, 0.0811261),
    (0.1716951, 0.08223631),
    (0.1841905, 0.08311282),
    (0.1968612, 0.08377811),
    (0.2096732, 0.0842591),
    (0.2226005, 0.08458639),
    (0.2357502, 0.08477819),
    (0.2491587, 0.08483614),
    (0.2628129, 0.08476187),
    (0.2766992, 0.08455741),
    (0.290804, 0.08422519),
    (0.3051134, 0.08376798),
    (0.3196132, 0.08318892),
    (0.3342893, 0.08249147),
    (0.3491272, 0.08167938),
    (0.3641125, 0.0807567),
    (0.3792305, 0.07972772),
    (0.3944665, 0.07859697),
    (0.4098055, 0.07736915),
    (0.4252326, 0.07604916),
    (0.440733, 0.07464201),
    (0.4562913, 0.07315285),
    (0.4718927, 0.07158688),
    (0.4875218, 0.06994939),
    (0.5031637, 0.06824569),
    (0.518803, 0.0664811),
    (0.5344246, 0.06466091),
    (0.5500133, 0.06279039),
    (0.5655542, 0.06087477),
    (0.581032, 0.05891918),
    (0.5964318, 0.05692868),
    (0.6117386, 0.05490826),
    (0.6269376, 0.05286275),
    (0.642014, 0.05079692),
    (0.6569532, 0.04871539),
    (0.6717406, 0.04662266),
    (0.6863619, 0.04452313),
    (0.7008028, 0.04242103),
    (0.7150492, 0.04032052),
    (0.7290872, 0.03822561),
    (0.7429032, 0.03614018),
    (0.7564835, 0.03406804),
    (0.769815, 0.03201287),
    (0.7828845, 0.02997823),
    (0.7956792, 0.02796763),
    (0.8081865, 0.02598447),
    (0.8203941, 0.02403205),
    (0.83229, 0.02211364),
    (0.8438624, 0.0202324),
    (0.8550998, 0.01839144),
    (0.8659912, 0.0165938),
    (0.8765257, 0.01484247),
    (0.8866929, 0.01314038),
    (0.8964826, 0.0114904),
    (0.9058851, 0.00989534),
    (0.914891, 0.00835793),
    (0.9234912, 0.00688088),
    (0.9316771, 0.0054668),
    (0.9394406, 0.00411822),
    (0.9467737, 0.00283762),
    (0.9536692, 0.00162736),
    (0.96012, 0.00048974),
    (0.9661197, -0.00057308),
    (0.9716621, -0.00155902),
    (0.9767416, -0.00246615),
    (0.981353, -0.00329264),
    (0.985492, -0.00403683),
    (0.989154, -0.00469719),
    (0.992335, -0.00527235),
    (0.995032, -0.00576111),
    (0.997243, -0.00616243),
    (0.998965, -0.00647546),
    (1.000196, -0.00669954),
    (1.000935, -0.00683418),
    (1.001174, -0.00687908),
    (1.000919, -0.00692149),
    (1.000178, -0.00704852),
    (0.998944, -0.00725975),
    (0.997219, -0.00755444),
    (0.995003, -0.00793157),
    (0.992299, -0.00838985),
    (0.98911, -0.0089277),
    (0.985438, -0.0095433),
    (0.981288, -0.01023457),
    (0.976662, -0.01099982),
    (0.9715658, -0.01183467),
    (0.9660039, -0.01273825),
    (0.9599817, -0.01370703),
    (0.9535049, -0.01473793),
    (0.9465799, -0.01582773),
    (0.9392132, -0.01697306),
    (0.931412, -0.01817046),
    (0.9231839, -0.01941634),
    (0.9145367, -0.02070707),
    (0.905479, -0.02203893),
    (0.8960195, -0.02340816),
    (0.8861674, -0.02481096),
    (0.8759324, -0.02624351),
    (0.8653245, -0.02770199),
    (0.8543541, -0.02918255),
    (0.8430318, -0.03068138),
    (0.831369, -0.03219466),
    (0.819377, -0.0337186),
    (0.8070677, -0.03524942),
    (0.7944532, -0.03678338),
    (0.781546, -0.03831674),
    (0.7683589, -0.0398458),
    (0.754905, -0.04136689),
    (0.7411976, -0.04287634),
    (0.7272504, -0.0443705),
    (0.7130772, -0.04584573),
    (0.6986922, -0.04729842),
    (0.6841098, -0.04872492),
    (0.6693444, -0.05012161),
    (0.6544109, -0.05148486),
    (0.6393242, -0.05281102),
    (0.6240994, -0.05409644),
    (0.6087517, -0.05533744),
    (0.5932966, -0.05653035),
    (0.5777496, -0.05767146),
    (0.5621262, -0.05875706),
    (0.5464421, -0.05978344),
    (0.530713, -0.06074688),
    (0.5149549, -0.06164366),
    (0.4991834, -0.06247009),
    (0.4834145, -0.0632225),
    (0.4676639, -0.06389723),
    (0.4519474, -0.06449072),
    (0.4362809, -0.06499944),
    (0.42068, -0.06541996),
    (0.4051603, -0.06574895),
    (0.3897374, -0.0659832),
    (0.3744267, -0.06611965),
    (0.3592435, -0.06615539),
    (0.3442029, -0.0660877),
    (0.3293199, -0.06591406),
    (0.3146093, -0.06563219),
    (0.3000858, -0.06524003),
    (0.2857638, -0.06473579),
    (0.2716573, -0.06411797),
    (0.2577805, -0.06338537),
    (0.244147, -0.06253707),
    (0.2307701, -0.0615725),
    (0.2176632, -0.06049142),
    (0.2048887, -0.05929765),
    (0.1925789, -0.05801619),
    (0.1807326, -0.05667411),
    (0.1693401, -0.05529339),
    (0.1583903, -0.05389139),
    (0.1478707, -0.05248135),
    (0.137768, -0.05107275),
    (0.1280683, -0.04967184),
    (0.1187575, -0.04828195),
    (0.1098217, -0.04690393),
    (0.1012477, -0.04553649),
    (0.09302314, -0.04417641),
    (0.08513727, -0.04281883),
    (0.07758103, -0.04145742),
    (0.07034743, -0.04008448),
    (0.06343174, -0.03869108),
    (0.05683164, -0.03726712),
    (0.05054721, -0.03580145),
    (0.04458092, -0.03428196),
    (0.03893754, -0.03269569),
    (0.03362391, -0.03102897),
    (0.02864879, -0.02926763),
    (0.02402257, -0.02739722),
    (0.01975707, -0.02540322),
    (0.01586521, -0.02327131),
    (0.01236085, -0.02098767),
    (0.00925853, -0.01853924),
    (0.00657326, -0.01591403),
    (0.00432035, -0.01310137),
    (0.00251528, -0.01009215),
    (0.00117354, -0.00687908),
    (0.00032524, -0.00350116),
    (0.0, 0.0)
]
# Separate x and y coordinates
x_values, y_values = zip(*points)

# Find the maximum x value
max_x = max(x_values)

# Calculate the factor to transform the maximum x to 12.5
factor = 12.5 / max_x

# # Multiply all x and y values by the calculated factor
# x_values = [x * factor for x in x_values]
# y_values = [y * factor for y in y_values]

# modified_points = [(x, y) for x, y in zip(x_values, y_values)]

# # Generate more z values for smoother representation
# z_values = np.linspace(0, 6, 10000)

# # Create a 3D plot
# fig = plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
# ax = fig.add_subplot(111, projection='3d')

# # Plot all (x, y) values for each z value
# for z in z_values:
#     ax.plot(x_values, y_values, z, marker='', linestyle='-')

# # Set plot title and labels
# ax.set_title('3D Plot of Points with Varying Z-values')
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')

# # Set x-axis ticks and grid in increments of 0.01
# x_ticks = np.arange(0, 12.51, 0.5)
# ax.set_xticks(x_ticks)
# ax.set_xticklabels(["{:.2f}".format(tick) for tick in x_ticks], rotation=45)

# # Set y-axis ticks and grid to match x-axis
# y_ticks = np.arange(min(y_values), max(y_values) + 0.01, 0.01)
# ax.set_yticks(y_ticks)
# ax.set_yticklabels(["{:.2f}".format(tick) for tick in y_ticks], rotation=45)

# # Ensure equal aspect ratio
# ax.set_box_aspect([np.ptp(arr) for arr in [x_values, y_values, z_values]])

# # Show the plot
# plt.show()

# def calculate_area(modified_points):
#     sum = 0
#     for i in range(len(modified_points)-1):
#          sum += sqrt((modified_points[i][0] - modified_points[i + 1][0])**2 + (modified_points[i][1] - modified_points[i + 1][1])**2)
#     area = sum * 150
#     return area

# # Calculate area
# area = calculate_area(modified_points)
# print("Area of the closed figure:", area)

#Calculus of thickness
max_y = max(y_values)*factor
min_y = min(y_values)*factor
thickness = max_y-min_y
print(thickness)