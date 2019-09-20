import math
import numpy as np
from matplotlib import pyplot as plt 

# SC for Steering Command

def applySC(pos, vl, vr, t, l):
    x = pos[0]
    y = pos[1]
    theta = pos[2]
    if (vl == vr):
        return np.array([x + np.cos(theta) * vr * t, y + np.sin(theta) * vr * t, theta])
    else:
        radius = l/2 * (vl+vr)/(vr-vl)
        omega = (vr + vl)/2

        # finding the rotation point
        iccX = x - radius * np.sin(theta)
        iccY = y + radius * np.cos(theta)

        # rotation matrix
        rotMatrix = np.array([[np.cos(omega*t), -np.sin(omega*t), 0],
                     [np.sin(omega*t), np.cos(omega*t), 0],
                     [0, 0, 1]])

        iccRobotPosition = np.array([x-iccX, y - iccY, theta])
        translationTerm = np.array([iccX, iccY, omega+t])

        newPos = np.add(np.dot(rotMatrix, iccRobotPosition), translationTerm)

        return newPos
