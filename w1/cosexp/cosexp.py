import numpy as np
import matplotlib.pyplot as plt
import math
import sys

def cosexp(x):
  return math.cos(x)*math.exp(x)

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
vCosexp = np.vectorize(cosexp)

y = vCosexp(x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x', ylabel='f(x)',
       title='f(x) = cos(x) * exp(x)')
ax.grid()

fig.savefig("cosexp.png")
plt.show()
