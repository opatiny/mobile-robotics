import math
import numpy as np
from matplotlib import pyplot as plt 

scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-math.pi/2, math.pi/2,
                    np.shape(scan)[0], endpoint='true')



plt.title('Data in the frame of reference of the laser range finder')
plt.polar(angle, scan, '.k', markersize=3)
plt.polar(0, 0, '+r', markersize=15) # laser range finder position
plt.savefig("results/polarLaserScan.png")
plt.savefig("results/polarLaserScan.svg")
plt.show()