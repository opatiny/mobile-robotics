# Week 5 - Probabilistic Motion Models

[Home](../../../../README.md) | [Mobile Robotics](../mobileRobotics.md)

Looking at the implementation of Bayes filters:
$$Bel(x_t) = \eta P(z_t| x_t) \Sigma_{x_{t-1}} P(x_t|u_t, x_{t-1}) Bel(x_{t-1})$$

- $P(z_t| x_t)$ : perception model
- $P(x_t|u_t, x_{t-1})$ : **motion model** (or transition model)
- $Bel(x_{t-1})$ : Belief

## Goal of the chapter

**Definition:** The motion model is the probability to be in a certain state given the previous state and the action performed.

**Goal:** Implement the motion model as a function. This function would have this prototype:

```python
double MM( pose x_t, odometry u_t, pose x_{t-1}); # returns a probability to be in a certain position
pose mm(odometry u_t, pose x_t); # returns a prediction for a future position
```
(we will do both)

`pose` would be a struct/object with three properties: $x$, $y$, $theta$.

We want this function to return a sample of a real-life distribution of poses (-> Gaussian).

## Typical motion models

- **Odometry-based:** incremental angle changes of the wheels
- **Velocity-based:** based on the velocity of the wheels

**Odometry:** Use of data from motion sensors to estimate change in position over time. (Wikipedia)

## Wheel encoders

The wheel encoder returns a digital signal. One kind of encoder just measures transitions from white to black on a striped disk fixed on the wheel (-> optical sensor). The resolution is limited by the amount of stripes?

## Reasons for motion errors of wheeled robots

- different wheels diameter
- bumps
- carpet/floor surface

## Dead Reckoning

**Definition:** Estimating a value of a variable quantity by using an earlier state and adding changes that occurred in the meantime. (Wikipedia)

## Odometry-Based model

- Robot moves from $x_{t_1} = \langle \bar{x}, \bar{y}, \bar{\theta} \rangle$ to $x_t = \langle \bar{x}', \bar{y}', \bar{\theta}' \rangle$
- Odometry information: every change in pose can be expressed by three parameters, a first angle, a distance and a second angle. => $u = \langle \delta_{rot1}, \delta_{trans}, \delta{rot2} \rangle$ where  
  $\delta_{trans} = \sqrt{(\bar{x}' - \bar{x})^2 + (\bar{x}' - \bar{x})^2}$ (Euclidian distance)

  $\delta_{rot1} = atan2(\bar{x}' - \bar{x}, + \bar{x}' - \bar{x}) -\bar{\theta}$

  $\delta_{rot2} = \bar{\theta}' - \bar{\theta} - \delta_{rot1}$

  Where $atan2()$ extends the inverse tangent and copes with the signs of x and y (standard in many programming languages).

**How we proceed:** Calculate the exact odometry that would take us from $x_{t-1}$ to $x_t$ and compare it to the measured odometry.

We want to know what is the probability of $u_t$ given $u_t'$.

## Noise model for odometry

The measured motion is the desired actual motion corrupted with noise. Whe need a model for the noise. Obviously the error on each parameter is proportional to it (p. ex. rotating longer -> bigger error on rotation). But the other parameters sometimes also influence. -> Rotating longer also results in a lateral shift.

We set:
- error on the initial rotation varies on: $\delta_{rot1}$, $\delta_{trans}$
- error on the translation varies on: $\delta_{rot1}$, $\delta_{trans}$, $\delta_{trans}$
- error on the final rotation varies on: $\delta_{rot2}$, $\delta_{trans}$

We can use different distributions for the error: Gaussian distribution, triangular distribution (fast, low calculation power).

The way you know the error parameters in real life would be my making the robot make the same movement many times and plotting where it ends. Then tune the parameters until the sampling you get represents reality.

## Sample-Based Density Representation

You take a plot and reduce it from one dimension and you represent that dimension by a set of samples whish density reflects the shape of the plot. -> We want to get samples form a distribution.

You can make easy operations on a uniform random distribution to obtain a sample of a normal distribution or a triangular distribution.
 This is very fast.

Normal distribution:

<img src="https://tex.cheminfo.org/?tex=%5Cfrac%7B1%7D%7B2%7D%5Csum%5Climits_%7Bi%3D1%7D%5E%7B12%7D%20rand(-b%2C%20b)"/>

Triangular distribution:

<img src="https://tex.cheminfo.org/?tex=%5Cfrac%7B%5Csqrt%7B6%7D%7D%7B2%7D%20%5B%20rand(-b%2C%20b)%20%2B%20rand(-b%2C%20b)%5D"/>

Where $b$ is the standard deviation of the distribution (interval over which you want the sampling?).

### Rejection sampling

How to obtain samples from an arbitrary function?
- Sample $x$ from a uniform distribution from $[-b, b]$
- Sample $y$ from $[0, max f]$
- if $f(x) > y$ keep sample $x$, otherwise reject it

## Velocity-Based Model

- basically the same as odometry-based
- measured motion = true motion + noise
- the action $u$ is defined by two parameters: $v$ and $\omega$, translation and rotation velocities
- -> 2 parameters in 3 dimensional space -> robot always in the direction of the arc it moves on -> we have to add an additional angle to add errors along the third dimension (sideways rotations)

## General remarks

The better the model, the better the Bayesian filtering in the end -> one must spend a lot of time on having accurate models for all situations (example: car -> model for rain, snow, ice, ...).

**Landmark:** A distinct object that allows to know the exact position of the system.

The motion model is important because robots cannot go through walls. -> if you have background knowledge about the environment, you can make a map-consistent motion model. -> the robot cannot be where a wall is

Be extremely careful about al the assumptions that you make.
