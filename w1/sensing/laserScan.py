import math
import numpy as np
scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-math.pi/2, math.pi/2,
                    np.shape(scan)[0], endpoint='true')