import numpy as np
import matplotlib.pyplot as plt
import math
import sys

normalArray = np.random.normal(5, 2, 10000)


plt.hist(normalArray, 50, density=True, facecolor='g', alpha=0.75)
plt.ylabel('Probability')
plt.title('Histogram of normal distribution')
plt.savefig("normal.png")
