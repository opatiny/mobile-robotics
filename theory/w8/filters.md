# Week 8 - Bayes Filter - Discrete Filters

[Week 7](../w7/probabilistic-motion-models.md) | [Mobile Robotics](../mobileRobotics.md) | [Week 9]()

Bayes filters:
$$Bel(x_t) = \eta P(z_t| x_t) \Sigma_{x_{t-1}} P(x_t|u_t, x_{t-1}) Bel(x_{t-1})$$

This week, we are interested in the Belief itself.

We are going to see three different implementations of the belief.

## Today's representation

An arbitrary function can be approximated by a histogram. We will talk about a discrete representation of the belief today. Then, the integral of the function would become a sum. 

There is no close formed representation for the belief -> it's complex. The only way you can approximately do that is to use the gaussian function.

## What is a convolution?

*All taken from Wiki*

In mathematics (in particular, functional analysis) convolution is a mathematical operation on two functions (f and g) that produces a third function expressing how the shape of one is modified by the other. The term convolution refers to both the result function and to the process of computing it. It is defined as the integral of the product of the two functions after one is reversed and shifted.

The convolution of f and g is written f∗g, using an asterisk. It is defined as the integral of the product of the two functions after one is reversed and shifted. As such, it is a particular kind of integral transform:

<img src="https://tex.cheminfo.org/?tex=(f*g)(t)%5Ctriangleq%20%5Cint%20_%7B-%5Cinfty%20%7D%5E%7B%5Cinfty%20%7D%20f(%5Ctau%20)g(t-%5Ctau%20)d%5Ctau%0A"/>

## What do we do when calculating the belief

- Start with a uniform distribution (uniform prior)
- Based on a first measurement: calculate the probability of a position depending on the measurement
- At a second position: probability to be at a certain position (independently from first measurement) -> function is smoother than the first one due to uncertainty on the action
- Combine both probabilities and normalize

## Discrete Bayes filter algorithm 

Slide 4

There is a for loop because there is a limited number of positions (discrete case). It has a $O(n^2)$ where $n$ is the number of "bins" of the histogram -> lot of power and lot of storage.

- We assume we have a robot living on a plane.
- We have a map of that plane
- The plane has three dimensions: x, y and the orientation -> we need a histogram with 3 dimensions - 
- We consider a discretisation of 10 cm for x and y and 1 degree for the orientation -> in a building of 20x50m, we have approx 4 millions bins -> 16Mb, 4 millions multiplications

## Observations on th belief

- in general, over time, the belief concentrates on where the robot actually is 
- -> one approach is only to update subspaces 
- -> you have to know if the robot is de-localized
- -> you can monitor the sensor model, and if it drops under a certain value, you know something has gone wrong and you have to evaluate the whole space
- the robot has to be able to unlearn it's current belief in case it is suddenly moved from one place to another