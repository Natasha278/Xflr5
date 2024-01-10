import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import numpy as np

# Your data points
points = [
    (1.0000000, 0.0019950),
    (0.9974774, 0.0026102),
    (0.9929085, 0.0037201),
    (0.9870521, 0.0051346),
    (0.9801884, 0.0067806),
    (0.9724844, 0.0086133),
    (0.9640559, 0.0106007),
    (0.9549902, 0.0127181),
    (0.9453566, 0.0149454),
    (0.9352124, 0.0172661),
    (0.9246063, 0.0196658),
    (0.9135802, 0.0221320),
    (0.9021712, 0.0246540),
    (0.8904123, 0.0272220),
    (0.8783331, 0.0298273),
    (0.8659609, 0.0324621),
    (0.8533205, 0.0351193),
    (0.8404347, 0.0377922),
    (0.8273250, 0.0404750),
    (0.8140113, 0.0431621),
    (0.8005122, 0.0458483),
    (0.7868454, 0.0485287),
    (0.7730275, 0.0511988),
    (0.7590742, 0.0538543),
    (0.7450005, 0.0564910),
    (0.7308209, 0.0591049),
    (0.7165489, 0.0616923),
    (0.7021977, 0.0642494),
    (0.6877799, 0.0667727),
    (0.6733075, 0.0692585),
    (0.6587922, 0.0717035),
    (0.6442453, 0.0741042),
    (0.6296777, 0.0764574),
    (0.6150998, 0.0787595),
    (0.6005219, 0.0810074),
    (0.5859539, 0.0831978),
    (0.5714054, 0.0853275),
    (0.5568856, 0.0873931),
    (0.5424038, 0.0893916),
    (0.5279688, 0.0913198),
    (0.5135891, 0.0931744),
    (0.4992733, 0.0949526),
    (0.4850295, 0.0966511),
    (0.4708659, 0.0982670),
    (0.4567901, 0.0997975),
    (0.4428100, 0.1012395),
    (0.4289331, 0.1025903),
    (0.4151667, 0.1038473),
    (0.4015181, 0.1050077),
    (0.3879944, 0.1060691),
    (0.3746025, 0.1070291),
    (0.3613493, 0.1078854),
    (0.3482415, 0.1086359),
    (0.3352856, 0.1092785),
    (0.3224882, 0.1098114),
    (0.3098556, 0.1102329),
    (0.2973941, 0.1105415),
    (0.2851099, 0.1107357),
    (0.2730090, 0.1108144),
    (0.2610975, 0.1107765),
    (0.2493812, 0.1106213),
    (0.2378660, 0.1103481),
    (0.2265575, 0.1099564),
    (0.2154615, 0.1094460),
    (0.2045835, 0.1088168),
    (0.1939290, 0.1080673),
    (0.1835034, 0.1071845),
    (0.1733122, 0.1061526),
    (0.1633605, 0.1049581),
    (0.1536536, 0.1035901),
    (0.1441967, 0.1020404),
    (0.1349949, 0.1003027),
    (0.1260533, 0.0983734),
    (0.1173767, 0.0962508),
    (0.1089702, 0.0939354),
    (0.1008386, 0.0914296),
    (0.0929867, 0.0887377),
    (0.0854193, 0.0858655),
    (0.0781412, 0.0828205),
    (0.0711569, 0.0796115),
    (0.0644712, 0.0762486),
    (0.0580885, 0.0727428),
    (0.0520135, 0.0691062),
    (0.0462506, 0.0653516),
    (0.0408043, 0.0614924),
    (0.0356789, 0.0575423),
    (0.0308789, 0.0535154),
    (0.0264085, 0.0494259),
    (0.0222721, 0.0452876),
    (0.0184738, 0.0411143),
    (0.0150180, 0.0369195),
    (0.0119087, 0.0327159),
    (0.0091501, 0.0285156),
    (0.0067463, 0.0243297),
    (0.0047014, 0.0201683),
    (0.0030194, 0.0160406),
    (0.0017043, 0.0119543),
    (0.0007601, 0.0079158),
    (0.0001907, 0.0039299),
    (0.0000000, 0.0000000),
    (0.0001907, -0.0038137),
    (0.0007601, -0.0074539),
    (0.0017043, -0.0109238),
    (0.0030194, -0.0142276),
    (0.0047014, -0.0173706),
    (0.0067463, -0.0203587),
    (0.0091501, -0.0231989),
    (0.0119087, -0.0258989),
    (0.0150180, -0.0284668),
    (0.0184738, -0.0309114),
    (0.0222721, -0.0332419),
    (0.0264085, -0.0354678),
    (0.0308789, -0.0375985),
    (0.0356789, -0.0396440),
    (0.0408043, -0.0416136),
    (0.0462506, -0.0435168),
    (0.0520135, -0.0453626),
    (0.0580885, -0.0471597),
    (0.0644712, -0.0489159),
    (0.0711569, -0.0506384),
    (0.0781412, -0.0523338),
    (0.0854193, -0.0540072),
    (0.0929867, -0.0556630),
    (0.1008386, -0.0573043),
    (0.1089702, -0.0589325),
    (0.1173767, -0.0605481),
    (0.1260533, -0.0621494),
    (0.1349949, -0.0637336),
    (0.1441967, -0.0652956),
    (0.1536536, -0.0668289),
    (0.1633605, -0.0683245),
    (0.1733122, -0.0697719),
    (0.1835034, -0.0711582),
    (0.1939290, -0.0724683),
    (0.2045835, -0.0736851),
    (0.2154615, -0.0747947),
    (0.2265575, -0.0757952),
    (0.2378660, -0.0766864),
    (0.2493812, -0.0774682),
    (0.2610975, -0.0781409),
    (0.2730090, -0.0787048),
    (0.2851099, -0.0791606),
    (0.2973941, -0.0795090),
    (0.3098556, -0.0797508),
    (0.3224882, -0.0798873),
    (0.3352856, -0.0799196),
    (0.3482415, -0.0798492),
    (0.3613493, -0.0796777),
    (0.3746025, -0.0794067),
    (0.3879944, -0.0790382),
    (0.4015181, -0.0785741),
    (0.4151667, -0.0780165),
    (0.4289331, -0.0773676),
    (0.4428100, -0.0766297),
    (0.4567901, -0.0758051),
    (0.4708659, -0.0748964),
    (0.4850295, -0.0739060),
    (0.4992733, -0.0728366),
    (0.5135891, -0.0716908),
    (0.5279688, -0.0704712),
    (0.5424038, -0.0691806),
    (0.5568856, -0.0678218),
    (0.5714054, -0.0663974),
    (0.5859539, -0.0649104),
    (0.6005219, -0.0633634),
    (0.6150998, -0.0617594),
    (0.6296777, -0.0601011),
    (0.6442453, -0.0583914),
    (0.6587922, -0.0566331),
    (0.6733075, -0.0548292),
    (0.6877799, -0.0529826),
    (0.7021977, -0.0510962),
    (0.7165489, -0.0491729),
    (0.7308209, -0.0472159),
    (0.7450005, -0.0452282),
    (0.7590742, -0.0432132),
    (0.7730275, -0.0411740),
    (0.7868454, -0.0391142),
    (0.8005122, -0.0370374),
    (0.8140113, -0.0349474),
    (0.8273250, -0.0328484),
    (0.8404347, -0.0307446),
    (0.8533205, -0.0286408),
    (0.8659609, -0.0265419),
    (0.8783331, -0.0244536),
    (0.8904123, -0.0223818),
    (0.9021712, -0.0203332),
    (0.9135802, -0.0183151),
    (0.9246063, -0.0163358),
    (0.9352124, -0.0144046),
    (0.9453566, -0.0125320),
    (0.9549902, -0.0107301),
    (0.9640559, -0.0090131),
    (0.9724844, -0.0073980),
    (0.9801884, -0.0059055),
    (0.9870521, -0.0045627),
    (0.9929085, -0.0034069),
    (0.9974774, -0.0024988),
    (1.0000000, -0.0019950)
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