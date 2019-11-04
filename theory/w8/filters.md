# Week 8 - Bayes Filter - Discrete Filters

[Week 7](../w7/probabilistic-motion-models.md) | [Mobile Robotics](../mobileRobotics.md) | [Week 9]()

Bayes filters:
$$Bel(x_t) = \eta P(z_t| x_t) \Sigma_{x_{t-1}} P(x_t|u_t, x_{t-1}) Bel(x_{t-1})$$

This week, we are interested in the Belief itself.

We are going to see three different implementations of the belief.

## Todays representation

An arbitrary function can be approximated by a histogram. We will talk about a discrete representation of the belief today.

