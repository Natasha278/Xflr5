import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import numpy as np

# Your data points
points = [
    (1.0000000, 0.0006300),
    (0.9974774, 0.0008624),
    (0.9929085, 0.0012819),
    (0.9870521, 0.0018171),
    (0.9801884, 0.0024406),
    (0.9724844, 0.0031357),
    (0.9640559, 0.0038907),
    (0.9549902, 0.0046963),
    (0.9453566, 0.0055453),
    (0.9352124, 0.0064314),
    (0.9246063, 0.0073494),
    (0.9135802, 0.0082949),
    (0.9021712, 0.0092637),
    (0.8904123, 0.0102523),
    (0.8783331, 0.0112575),
    (0.8659609, 0.0122765),
    (0.8533205, 0.0133066),
    (0.8404347, 0.0143454),
    (0.8273250, 0.0153907),
    (0.8140113, 0.0164404),
    (0.8005122, 0.0174927),
    (0.7868454, 0.0185456),
    (0.7730275, 0.0195976),
    (0.7590742, 0.0206470),
    (0.7450005, 0.0216923),
    (0.7308209, 0.0227320),
    (0.7165489, 0.0237647),
    (0.7021977, 0.0247891),
    (0.6877799, 0.0258038),
    (0.6733075, 0.0268074),
    (0.6587922, 0.0277989),
    (0.6442453, 0.0287768),
    (0.6296777, 0.0297400),
    (0.6150998, 0.0306873),
    (0.6005219, 0.0316174),
    (0.5859539, 0.0325292),
    (0.5714054, 0.0334216),
    (0.5568856, 0.0342933),
    (0.5424038, 0.0351432),
    (0.5279688, 0.0359702),
    (0.5135891, 0.0367732),
    (0.4992733, 0.0375510),
    (0.4850295, 0.0383026),
    (0.4708659, 0.0390269),
    (0.4567901, 0.0397229),
    (0.4428100, 0.0403895),
    (0.4289331, 0.0410258),
    (0.4151667, 0.0416307),
    (0.4015181, 0.0422034),
    (0.3879944, 0.0427429),
    (0.3746025, 0.0432484),
    (0.3613493, 0.0437191),
    (0.3482415, 0.0441542),
    (0.3352856, 0.0445528),
    (0.3224882, 0.0449145),
    (0.3098556, 0.0452385),
    (0.2973941, 0.0455242),
    (0.2851099, 0.0457712),
    (0.2730090, 0.0459789),
    (0.2610975, 0.0461469),
    (0.2493812, 0.0462749),
    (0.2378660, 0.0463626),
    (0.2265575, 0.0464098),
    (0.2154615, 0.0464163),
    (0.2045835, 0.0463820),
    (0.1939290, 0.0463051),
    (0.1835034, 0.0461725),
    (0.1733122, 0.0459679),
    (0.1633605, 0.0456772),
    (0.1536536, 0.0452889),
    (0.1441967, 0.0447938),
    (0.1349949, 0.0441850),
    (0.1260533, 0.0434577),
    (0.1173767, 0.0426091),
    (0.1089702, 0.0416385),
    (0.1008386, 0.0405470),
    (0.0929867, 0.0393375),
    (0.0854193, 0.0380143),
    (0.0781412, 0.0365835),
    (0.0711569, 0.0350523),
    (0.0644712, 0.0334292),
    (0.0580885, 0.0317235),
    (0.0520135, 0.0299458),
    (0.0462506, 0.0281072),
    (0.0408043, 0.0262193),
    (0.0356789, 0.0242944),
    (0.0308789, 0.0223449),
    (0.0264085, 0.0203833),
    (0.0222721, 0.0184222),
    (0.0184738, 0.0164739),
    (0.0150180, 0.0145505),
    (0.0119087, 0.0126635),
    (0.0091501, 0.0108238),
    (0.0067463, 0.0090415),
    (0.0047014, 0.0073261),
    (0.0030194, 0.0056857),
    (0.0017043, 0.0041276),
    (0.0007601, 0.0026577),
    (0.0001907, 0.0012808),
    (0.0000000, 0.0000000),
    (0.0001907, -0.0011646),
    (0.0007601, -0.0021958),
    (0.0017043, -0.0030971),
    (0.0030194, -0.0038727),
    (0.0047014, -0.0045283),
    (0.0067463, -0.0050706),
    (0.0091501, -0.0055071),
    (0.0119087, -0.0058465),
    (0.0150180, -0.0060978),
    (0.0184738, -0.0062710),
    (0.0222721, -0.0063766),
    (0.0264085, -0.0064252),
    (0.0308789, -0.0064280),
    (0.0356789, -0.0063960),
    (0.0408043, -0.0063405),
    (0.0462506, -0.0062723),
    (0.0520135, -0.0062022),
    (0.0580885, -0.0061404),
    (0.0644712, -0.0060965),
    (0.0711569, -0.0060792),
    (0.0781412, -0.0060968),
    (0.0854193, -0.0061560),
    (0.0929867, -0.0062628),
    (0.1008386, -0.0064216),
    (0.1089702, -0.0066356),
    (0.1173767, -0.0069064),
    (0.1260533, -0.0072337),
    (0.1349949, -0.0076159),
    (0.1441967, -0.0080491),
    (0.1536536, -0.0085276),
    (0.1633605, -0.0090436),
    (0.1733122, -0.0095872),
    (0.1835034, -0.0101462),
    (0.1939290, -0.0107061),
    (0.2045835, -0.0112502),
    (0.2154615, -0.0117650),
    (0.2265575, -0.0122486),
    (0.2378660, -0.0127009),
    (0.2493812, -0.0131218),
    (0.2610975, -0.0135112),
    (0.2730090, -0.0138693),
    (0.2851099, -0.0141961),
    (0.2973941, -0.0144917),
    (0.3098556, -0.0147564),
    (0.3224882, -0.0149903),
    (0.3352856, -0.0151939),
    (0.3482415, -0.0153675),
    (0.3613493, -0.0155114),
    (0.3746025, -0.0156260),
    (0.3879944, -0.0157120),
    (0.4015181, -0.0157698),
    (0.4151667, -0.0158000),
    (0.4289331, -0.0158030),
    (0.4428100, -0.0157797),
    (0.4567901, -0.0157306),
    (0.4708659, -0.0156563),
    (0.4850295, -0.0155575),
    (0.4992733, -0.0154350),
    (0.5135891, -0.0152895),
    (0.5279688, -0.0151217),
    (0.5424038, -0.0149322),
    (0.5568856, -0.0147219),
    (0.5714054, -0.0144915),
    (0.5859539, -0.0142418),
    (0.6005219, -0.0139734),
    (0.6150998, -0.0136871),
    (0.6296777, -0.0133837),
    (0.6442453, -0.0130639),
    (0.6587922, -0.0127285),
    (0.6733075, -0.0123782),
    (0.6877799, -0.0120137),
    (0.7021977, -0.0116358),
    (0.7165489, -0.0112453),
    (0.7308209, -0.0108430),
    (0.7450005, -0.0104296),
    (0.7590742, -0.0100059),
    (0.7730275, -0.0095728),
    (0.7868454, -0.0091311),
    (0.8005122, -0.0086818),
    (0.8140113, -0.0082257),
    (0.8273250, -0.0077641),
    (0.8404347, -0.0072978),
    (0.8533205, -0.0068281),
    (0.8659609, -0.0063563),
    (0.8783331, -0.0058838),
    (0.8904123, -0.0054121),
    (0.9021712, -0.0049428),
    (0.9135802, -0.0044779),
    (0.9246063, -0.0040195),
    (0.9352124, -0.0035699),
    (0.9453566, -0.0031318),
    (0.9549902, -0.0027083),
    (0.9640559, -0.0023031),
    (0.9724844, -0.0019204),
    (0.9801884, -0.0015655),
    (0.9870521, -0.0012452),
    (0.9929085, -0.0009687),
    (0.9974774, -0.0007510),
    (1.0000000, -0.0006300)
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
#          sum += sqrt((modified_points[i][0] - modified_points[i + 1][0])**2 + (modified_points[i][1] - modified_points[i+1][1])**2)
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


 