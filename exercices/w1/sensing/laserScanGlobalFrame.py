import math
import numpy as np
from matplotlib import pyplot as plt 
pi = math.pi

scan = np.loadtxt('laserscan.dat') # put values from a file in an array
angle = np.linspace(-math.pi/2, math.pi/2,
                    np.shape(scan)[0], endpoint='true') # equally spaced values in a range

# switch to cartesian coordinates
x = scan*np.cos(angle);
y = scan*np.sin(angle);

# transformation matrix from laser range finder to robot
T_R_L = np.array([[np.cos(pi), -np.sin(pi), 0.2],
                 [np.sin(pi), np.cos(pi), 0],
                 [0, 0, 1]])

# transformation matrix from robot to global (O)
T_O_R = np.array([[np.cos(pi/4), -np.sin(pi/4), 1],
                 [np.sin(pi/4), np.cos(pi/4), 0.5],
                 [0, 0, 1]])

# transformation matrix from laser range finder to global (O)
T_O_L = np.dot(T_O_R, T_R_L)

rowOnes = np.ones(len(x))
laserScan = np.array([x, y, rowOnes])
globalScan = np.dot(T_O_L, laserScan)


plt.title('Data in the global frame of reference')
plt.xlabel('x distance [m]')
plt.ylabel('y distance [m]')
plt.plot(globalScan[0], globalScan[1], '.k', markersize=3) # plot distance values in global frame

# global frame of reference
plt.plot(0, 0, '.g', markersize=6)
plt.text(-0.2 , 0.2, 'O', )

# robot position
plt.plot(T_O_R[0,2], T_O_R[1,2], '+b', markersize=15)

# laser range finder position
plt.plot(T_O_L[0,2], T_O_L[1,2], '+r', markersize=15)

plt.savefig("./results/laserScanGF.png")
plt.savefig("./results/laserScanGF.svg")
plt.show()