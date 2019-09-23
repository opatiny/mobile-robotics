import math
import numpy as np
from matplotlib import pyplot as plt 
pi = np.pi

# local imports
from getNewPos import applySC as applySC

l = 0.5 # [m]

pos = np.array([1.5, 2, pi/2])
plt.quiver(pos[0], pos[1], np.cos(pos[2]), np.sin(pos[2]))

pos1 = applySC(pos, 0.3, 0.3, 3, l)
plt.quiver(pos1[0], pos1[1], np.cos(pos1[2]), np.sin(pos1[2]))

pos2 = applySC(pos1, 0.1, -0.1, 1, l)
plt.quiver(pos2[0], pos2[1], np.cos(pos2[2]), np.sin(pos2[2]))

pos3 = applySC(pos2, 0.2, 0, 2, l)
plt.quiver(pos3[0], pos3[1], np.cos(pos3[2]), np.sin(pos3[2]))

plt.show()
print(pos)
print(pos1)
print(pos2)
print(pos3)
