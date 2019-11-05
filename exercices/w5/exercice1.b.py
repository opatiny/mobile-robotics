import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats
from mpl_toolkits import mplot3d
from matplotlib import cm

""" return the probability of a measurement given the actual location
    @param location (array of 2 elements: [x, y])
    @return: integer
"""
def pMeasurementGivenLocation(location):

    # towers locations
    t0 = np.array([12, 4])
    t1 = np.array([5, 7])

    # measurements made by the towers
    measurement0 = 3.9
    measurement1 = 4.5

    # towers noises (variance)
    n0 = 1
    n1 = 1.5

    # euclidean distances from towers to location
    d0 = np.linalg.norm(t0-location)
    d1 = np.linalg.norm(t1-location)

    # probabilities of a measurement for each tower
    p0 = scipy.stats.norm.pdf(measurement0, d0, math.sqrt(n0))
    p1 = scipy.stats.norm.pdf(measurement1, d1, math.sqrt(n1))

    return p0 * p1


#locations of interest
m_0 = np.array([10,8]) # uni
m_1 = np.array([6,3]) # home
x_0 = np.array([12,4]) # tower 0
x_1 = np.array([5,7]) # tower 1

# creating a 2D grid
x = np.arange(3.0,15.0,0.5)
y = np.arange(-5.0,15.0,0.5)
X,Y = np.meshgrid(x,y)

#calculate likelihood for each position
z = np.array([pMeasurementGivenLocation(np.array([x,y])) for x, y in zip(X.flatten(), Y.flatten())])
Z = z.reshape(X.shape)

# plot
fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, alpha=0.9)
ax.contour3D(X, Y, Z, 40, cmap=cm.inferno)

ax.scatter(m_0[0], m_0[1], pMeasurementGivenLocation(m_0), c='g', marker='o', s=100)
ax.scatter(m_1[0], m_1[1], pMeasurementGivenLocation(m_1), c='r', marker='o', s=100)
ax.scatter(x_0[0], x_0[1], pMeasurementGivenLocation(x_0), c='g', marker='^', s=100)
ax.scatter(x_1[0], x_1[1], pMeasurementGivenLocation(x_1), c='r', marker='^', s=100)

ax.set_xlabel('m_x')
ax.set_ylabel('m_y')
ax.set_zlabel('likelihood')

plt.show()
