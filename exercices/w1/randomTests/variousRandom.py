import numpy as np
import matplotlib.pyplot as plt
import math
import sys

np.random.seed(42)

normalArray = np.random.normal(5, 2, 10000)
uniformArray = np.random.uniform(0, 10, 10000)

normalMean = np.mean(normalArray)
uniformMean = np.mean(uniformArray)

print("normal :", normalMean, "    uniform :", uniformMean)

normalSD = np.std(normalArray)
uniformSD = np.std(uniformArray)

print("normal :", normalSD, "    uniform :", uniformSD)
# the standard deviation of the uniform array is bigger,
# because the mean "distance" the average of the array is
# bigger than in the normal distribution

#plotting histograms of the arrays

plt.hist(normalArray, 50, density=True, facecolor='g', alpha=0.75)
plt.ylabel('Probability')
plt.title('Histogram of normal distribution')
plt.savefig("normal.png")

plt.clf()
plt.cla()
plt.close()

plt.hist(uniformArray, 50, density=True, facecolor='g', alpha=0.75)
plt.ylabel('Probability')
plt.title('Histogram of uniform distribution')
plt.savefig("uniform.png")
