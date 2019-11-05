import math
import scipy.stats

# uni tower 0
a = scipy.stats.norm.pdf(3.9, 2*math.sqrt(5), 1)

# uni tower 1
b = scipy.stats.norm.pdf(4.5, math.sqrt(26), math.sqrt(1.5))

print(a*b)

# home tower 0
c = scipy.stats.norm.pdf(3.9, math.sqrt(37), 1)

# home tower 0
d = scipy.stats.norm.pdf(4.5, math.sqrt(17), math.sqrt(1.5))

print(c*d)
