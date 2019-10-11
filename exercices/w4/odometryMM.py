import numpy as np
import matplotlib.pyplot as plt
import math

from normalSample import normalSampleTwelve as normSample

# implementing an odometry-based motion model

# defining classes for pose and odometry
class Pose:
    def __init__(self, x = 0, y = 0, theta = 0):
        self.x = x
        self.y = y
        self.theta = theta

class Odometry:
    def __init__(self, rotDiff1 = 0, rotDiff2 = 0, translationDiff = 0):
        self.rotDiff1 = rotDiff1
        self.rotDiff2 = rotDiff2
        self.translationDiff = translationDiff

# initialPose = Pose() : initial pose
# odometry = Odometry() : odometry reading
# noise = [alpha1, alpha2, alpha3, alpha4] : noise

def newPoseOdometry(initialPose, odometry, noise):

    alpha1 = noise[0]
    alpha2 = noise[1]
    alpha3 = noise[2]
    alpha4 = noise[3]

    x = initialPose.x
    y = initialPose.y
    theta = initialPose.theta

    rotDiff1 = odometry.rotDiff1
    rotDiff2 = odometry.rotDiff2
    transDiff = odometry.translationDiff

    # calculating the odometry with its uncertainty (include noise)
    sigma1 = alpha1 * math.fabs(rotDiff1) + alpha2 * transDiff
    noiseRotDiff1 = rotDiff1 + normSample(0, sigma1)

    sigma2 = alpha1 * math.fabs(rotDiff2) + alpha2 * transDiff
    noiseRotDiff2 = rotDiff2 + normSample(0, sigma2)

    sigma3 = alpha3 * transDiff + alpha4 * (math.fabs(rotDiff1) + math.fabs(rotDiff2))
    noiseTransDiff = transDiff + normSample(0, sigma3)

    newPose = Pose()

    newPose.x = x + noiseTransDiff * math.cos(theta + noiseRotDiff1)
    newPose.y = y + noiseTransDiff * math.sin(theta + noiseRotDiff1)
    newPose.theta = theta + noiseRotDiff1 + noiseRotDiff2

    return newPose

origin = Pose(2, 4, 0)
odometry = Odometry(math.pi/2, 0, 1)
noise = [0.1, 0.1, 0.01, 0.01]

x = []
y= []

for i in range(5000):
    pose = newPoseOdometry(origin, odometry, noise)
    x = np.append(x, pose.x)
    y = np.append(y, pose.y)

plt.title('Input the same data 5000 times for odometry based motion model')
plt.xlabel('x distance [m]')
plt.ylabel('y distance [m]')
plt.plot(x, y, '.k', markersize=3) # plot distance values in global frame
plt.axis('scaled')

plt.show()