import math
import numpy as np
from matplotlib import pyplot as plt 
pi = np.pi

# local imports
from getNewPos import applySC as applySC

l = 0.5 # [m]

pos1 = applySC([1.5, 2, pi/2], 0.3, 0.3, 3, l)
pos2 = applySC(pos1, 0.1, -0.1, 1, l)
pos3 = applySC(pos2, 0.2, 0, 2, l)

print(pos3)
