import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import timeit

# mu: mean, sigma: standard deviation, returns a float

def normalSampleTwelve(mu, sigma):

    x = 0.5*np.sum(np.random.uniform(-sigma, sigma, 12))

    return mu + x

def rejection(mu, sigma):
    # interval from which samples are drawn
    interval = 5*sigma

    while True:
        x = np.random.uniform(mu - interval, mu + interval, 1)[0]
        y = np.random.uniform(0, bell(mu, mu, sigma), 1)[0]
        if y <= bell(x, mu, sigma):
            break
    return x

def bell(x, mu, sigma):
    return 1/(sigma* np.sqrt(2*np.pi)) * np.e **((x - mu)**2/(2*sigma**2))

# mu: mean, sigma: standard deviation, returns a float
def boxMuller(mu, sigma):
    u = np.random.uniform(0, 1, 2)

    x = np.cos(2*np.pi*u[0])*np.sqrt(-2*np.log(u[1]))

    return mu + sigma * x

### testing execution times with timeit

def samplingTime(mu, sigma, numberSamples, functionName):
    start = timeit.default_timer()
    for i in range(numberSamples):
        functionName(mu, sigma)
    end = timeit.default_timer()

    actualTime = (end-start)/ numberSamples * 1e6

    print("time in us to execute " + functionName.__name__ + ": ", actualTime)
    
'''
mu, sigma = 0, 1
sampleFunction = [
    normalSampleTwelve,
    rejection,
    boxMuller,
    np.random.normal
]

for fnc in sampleFunction:
    samplingTime(mu, sigma, 10000, fnc);
'''