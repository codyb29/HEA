import sys
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import statistics as stat


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

FILENAME = sys.argv[1]
X = []
Y = []
Z = []
COLOR = []
gen, ctr = 0, 1
with open(FILENAME, "r") as fl:
    for line in fl:
        data = line.split(' ')
        X.append(gen)
        Y.append(float(data[0])) # RMSD
        Z.append(float(data[1])) # Scores
        COLOR.append(float(data[2][:-1]))
        if (ctr % 100 == 0) :
            gen += 1
        ctr += 1

ax.set_zlim(-100, 100)
ax.set_xlim(0, 200)
ax.set_ylim(0, 25)

# Plot the surface.
dots = ax.scatter(X, Y, Z, c =COLOR, marker='.')

plt.title(FILENAME[:-4]+" Over the Generations")
ax.set_ylabel('Cα-RMSD')
ax.set_xlabel('Generation')
ax.set_zlabel('Rosetta score4 energy')

# Add a color bar which maps values to colors.
fig.colorbar(dots, shrink=0.5, aspect=5)

print('*********************************************')
print('RMSD statistical breakdown:')
print("Mean RMSD:\t" + str(stat.mean(Y)))
print("Median RMSD:\t" + str(stat.median(Y)))
print("Min RMSD:\t" + str(min(Y)))
print("Max RMSD:\t" + str(max(Y)))
print('*********************************************')
print('Pyrosetta score4 statistical breakdown:')
print("Mean score:\t" + str(stat.mean(Z)))
print("Median score:\t" + str(stat.median(Z)))
print("Min score:\t" + str(min(Z)))
print("Max score:\t" + str(max(Z)))
print('*********************************************')

plt.show()