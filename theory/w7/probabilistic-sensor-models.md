# Week 7 - Probabilistic Sensor Models

[Week 6](../w6/probabilistic-motion-models.md) | [Mobile Robotics](../mobileRobotics.md) | [Week 8]()

Bayes filters:
$$Bel(x_t) = \eta P(z_t| x_t) \Sigma_{x_{t-1}} P(x_t|u_t, x_{t-1}) Bel(x_{t-1})$$

This week, we are interested in the term $P(z_t| x_t)$ (**sensor model**).

You can have a very crapy sensor, but as long as it is better than random,  you gain some valuable information that you can use in calculation.

**Today's goal:** Be able to measure the uncertainty of a sensor.

## Sensors types

- **Contact sensor:** bumper -> interesting, because it gives a binary value -> some distance, or zero distance
- **Proprioceptive sensors:**
  - Accelerometer
  - Gyroscope
  - Compass,inclinometer
- **Proximity sensor:**
  - Sonar
  - Radar
  - Laser range-finder
  - Infrared
- **Visual sensors:** camera -> no direct distance measurement -> landmarks
- **Satellite-based sensors:** GPS -> unprecise, doesn't work indoors

## Goal

$P(z_t| x_t)$ : Determine the probability of a measurement $z$ given the robot position $x$.

 -> how to model this probability?

## Beam-based sensor model

- scan $z$ consists of $K$ measurements
  
  $z = \{z_1, z_2, ..., z_K\}$
- Independence assumption: The measurements are independent one from each other.
  -> we can calculate each probability independently from the others and then multiply them. This is a strong assumption -> it might be problematic in some cases.

  <img src="https://tex.cheminfo.org/?tex=P(z%20%7C%20x%2C%20m)%20%3D%20%5Cprod%5Climits_%7Bk%3D1%7D%5EK%20P(z_K%20%7C%20x%2C%20m)"/>

   Where $m$ is the map (prior knowledge on the environment), $z$: measurement, $x$: pose of the robot. -> localization in a known environment

### Typical measurement errors of range measurements

- crosstalk (especially with sonar)
- measurements shorter than expected -> dust or unexpected obstacle
- beams going through walls (often with sonar): can happen because que surface reflecting is at an angle too big -> light is reflect but never comes back to the sensor
- transparent obstacles

Noise caused by uncertainty:
- on distance measurement to known obstacle
- on known obstacle position
- on position of additional obstacle
- also, obstacle can be missed

### Beam-based proximity model

**Maximal range:** every sensor has a maximal range that is can output -> you know the maximal time that you have to wait for an echo to some back.

To know the global probability density function for a measurement (given the position of the robot is known), we have to combine four factors (**weighted sum**, ****"mixture density"):

1. The measurement noise: Gaussian distribution
2. Unexpected obstacles (whenever there is more than one, otherwise it would be uniform): inverse exponential distribution, and zero after a know obstacle
3. Random measurements: uniform distribution
4. Max range: zero everywhere, except one at the max range

<img src="https://tex.cheminfo.org/?tex=P(z%20%7C%20x%2C%20m)%20%3D%20%0A%5Cbegin%7Bpmatrix%7D%0A%5Calpha_%7Bhit%7D%5C%5C%0A%5Calpha_%7Bunexp%7D%20%5C%5C%0A%5Calpha_%7Bmax%7D%20%20%5C%5C%0A%5Calpha_%7Brand%7D%0A%5Cend%7Bpmatrix%7D%0A%5ET%0A%5Ccdot%0A%5Cbegin%7Bpmatrix%7D%0AP_%7Bhit%7D(z%20%7C%20x%2C%20m)%5C%5C%0AP_%7Bunexp%7D(z%20%7C%20x%2C%20m)%20%5C%5C%0AP_%7Bmax%7D(z%20%7C%20x%2C%20m)%20%20%5C%5C%0AP_%7Brand%7D(z%20%7C%20x%2C%20m)%0A%5Cend%7Bpmatrix%7D"/>

The function looks very different depending on the sensor and on the environment (-> slides 9 and 10). The alphas are the contribution of each error factor,

How to determine the model parameters (alphas and function related parameters)? -> calibration (test the sensor in known environment)

Then, an algorithm is used to optimize the parameters to fit the best the histogram of values generated before.

Algorithms examples (model continuous function from discrete measurements): 
- Hill climbing
- Gradient descent

### How to implement this?

We are looking for $P(z| x, m)$, but to make it easier, we calculate an expected measurement $z_{exp}$ from the pose, and then look for $P(z|z_{exp})$.
To make this more accurate, we can additionally calculate an expected angle, which informs on a probability of a total reflection (adding a dimension in calculation). Not that important for lidar

### Summary beam-based model

- Independence between beams is assumed (careful!)
- Mixture of different causes of uncertainty, which are considered to be independent (problematic?)
- Implementation: 
  - learn parameters based on real data
  - expected measurements could be pre-processed -> always the same compromise between memory and computation power
- Drawbacks:
  - not smooth
  - not very efficient

## Scan-based model

**Concept:** Not trying to follow a beam, just checking the endpoint.

Every known obstacle in the map gets a **likelihood fields** around it (gaussian distribution). All the other causes get a uniform distribution (e.g.: dynamic obstacles). Then, you take a top-bottom slice of the likelihood fields. which gives you the probability function (so the probability is higher the closest the beam is to an obstacle). 

-> how far is the beam from the obstacle(s)

This is a lot more efficient to compute than the previous approach. However, this model doesn't take into account all the physical properties of the world.
-> Solution: Instead of only calculating the end point, we could sample the beam.

### Scan matching

Being able to superpose two scans taken by two different sensors and be able to calculate the distance between the sensors.

Advantage, the scans with a likelihood field have a smooth probability gradient, which allows to follow the gradient to get to the closest obstacle.

### Properties of scan-based model

- efficient, 2D
- distance grid is smooth
- allows gradient descent and scan matching
- drawback: ignores some physical properties

## Features (sonar, laser, vision)

### Landmarks
**
Definition:** Distinct object in the world

Types:
- Active beacons -> things that emit signal
- Passive (an object you see, or that reflects)
- Standard approach: **triangulation**

The info that we can get:
- distance to the landmark
- and / or bearing in regard to the landmark (angle)

**VPS:** Visual Positioning System

### Landmark localization

We know the distance $d$ and the angle $\alpha$ to a landmark -> what is the probability to get a certain measurement? -> the landmark acts as a map.

$p(d, \alpha | x, m) = p(d | x, m) \cdot p(\alpha |x, m)$ -> independence assumption

Calculate the probability a distance is measured from each landmarks (-> circles). Multiply the probabilities of all the landmarks to get the intersection of them -> the most likely position where the robot was when it did these measurements.

## Summary

- it is important to have a model as good as possible for the sensor uncertainty
- always stay aware of the underlying assumptions!
