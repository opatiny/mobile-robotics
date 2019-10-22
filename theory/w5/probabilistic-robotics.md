# Week 5 - Probabilistic Robotics

[Week 4](../w4/proximity-sensors.md) | [Mobile Robotics](../mobileRobotics.md) | [Week 6](../w6/probabilistic-motion-models.md)

Goal: Get an "explicit representation of uncertainty"

## Axioms of Probability Theory

$P(A)$ denotes the probability that proposition $A$ is true.

- $0 \leq P(A) \leq 1$
- $P(True) = 1$ and $P(False) = 0$
- $P(A \vee B) = P(A) + P(B) - P(A \wedge B)$ ($\vee$ : or, $\wedge$ : and)

Probabilities are nothing else as frequencies.

## Derived equations

- $P(A) = 1 - P(\neg A)$

## Discrete random variables

- a random variable can take a countable number of values in a set ${x_1, x_2, ..., x_n}$
- $P(X=x_i) = P(x_i)$ : probability that a random variable $X$ takes the value $x_i$
- $P(.)$ : Probability mass function
- $\Sigma_x P(x) = 1$

## Continuous random variables

- The variable takes a value in the continuum
- probability density function :

  <img src="https://tex.cheminfo.org/?tex=P(x%20%5Cin%20%5Ba%2Cb%5D)%20%3D%20%5Cint_a%5Eb%20p(x)dx"/>

- $\int p(x)dx = 1$

## Joint and Conditional Probability

- $P(x =x \quad and \quad Y = y) = P(x, y)$
- If $X$ and $Y$ are independent: $P(x, y) = P(x)P(y)$
- $P(x|y)$ : probability of $x$ given $y$
- Definition:
  $$P(x|y) = P(x, y) / P(y)$$
  $$P(x, y) = P(x|y) P(y)$$

## Law of Total Probability

Discrete case :

$$P(x) = \Sigma_y P(x|y)P(y) =\Sigma_y P(x, y)$$

Continuous case :

$$p(x) = \int p(x|y)p(y) dy = \int p(x, y) dy$$

## Bayes Formula

From what we know from above, we can derive: $P(x, y) = P(x|y)P(y) = P(y|x)P(x)$

Which leads to Baye's theorem:

<img src="https://tex.cheminfo.org/?tex=P(x%7Cy)%20%3D%20%5Cfrac%7BP(y%7Cx)P(x)%7D%7BP(y)%7D%20%3D%20%5Cfrac%7Blikelihood%20%5C%3B%20%5Ccdot%20%5C%3B%20prior%7D%7Bevidence%7D"/>

## Baye's Rule with background knowledge

$z$ : some additional information

<img src="https://tex.cheminfo.org/?tex=P(x%7Cy%2Cz)%20%3D%20%5Cfrac%7BP(y%7Cx%2Cz)P(x%7Cz)%7D%7BP(y%7Cz)%7D"/>

This can be proved knowing what we have seen so far.

## Normalization

Give a way to find $P(y)$ -> it shows that we can deduce it from the rest.

<img src="https://tex.cheminfo.org/?tex=P(x%7Cy)%20%3D%20%5Cfrac%7BP(y%7Cx)P(x)%7D%7BP(y)%7D%20%3D%20%5Ceta%20P(y%7Cx)P(x)%20%5Cquad%20%5Ctextrm%7Bwhere%7D%20%5Cquad%20%5Ceta%20%3D%20P(y)%5E%7B-1%7D%20"/>

Therefore,

<img src="https://tex.cheminfo.org/?tex=P(y)%20%3D%20%5CSigma_x%20P(y%7Cx)P(x)"/>

**Remark:**

$\Sigma_y P(x|y)$ is not necessarily 1.

$\Sigma_x P(x|y) = 1$

## Conditional Independence

$$P(x,y|z) = P(x|z)P(y|z)$$

## Recursive Bayesian Updating

-> if we have additional information about the environment -> new measurements adding up ($z_i$) -> what is the probability that the door is open given my current measurement and all the previous ones

**Careful!!!** The previous measurement is a predictor for the current one in a normal world! -> Walls are continuous, so a sensor will have only small variations if the robot moves slightly -> dependence between the measurements!

<img src="https://tex.cheminfo.org/?tex=P(x%7Cz_1%2C%20...%2C%20z_n)%20%3D%20%5Cfrac%7BP(z_n%7Cx%2C%20z_1%2C%20...%2C%20z_%7Bn-1%7D)P(x%7Cz_1%2C%20...%2C%20z_%7Bn-1%7D)%7D%7BP(z_n%7Cz_1%2C%20...%2C%20z_%7Bn-1%7D)%7D"/>

**Markov assumption :** $z_n$ (measurement n) is independent of $z_1, ..., z_{n-1}$ (all the previous measurements) **if we know $x_n$** (the actual state of the robot).

Given this independence assumption, $P(z_n|x, z_1, ..., z_{n-1}) = P(z_n|x)$.

By replacing and simplifying, we get:

<img src="https://tex.cheminfo.org/?tex=P(x%7Cz_1%2C%20...%2C%20z_n)%20%3D%20%5Ceta_%7B1...n%7D%20%5CBig%5B%5Cprod_%7Bi%3D1...n%7DP(z_i%7Cx)%20%5CBig%5D%20P(x)"/>

## Actions

- the world is dynamic -> it changes (sometimes the robot acts on the environment) -> that must be taken into account
- actions carried out by the robot are never perfect -> they increase the uncertainty (**non-deterministic / stochastic system**)
- we use a likelihood function: what is the probability that I will end up with a certain state $x$ given that I executed a certain action $u$ and that I was previously in state $x'$. -> $P(x|u, x')$ (Action model)

### Law of Total Probability: Integrating the outcome of actions

Discrete case : 
$$P(x|u) = \Sigma P(x|u, x')P(x' | u) = \Sigma P(x|u, x')P(x')$$ 

Continuous case : 
$$p(x) = \int p(x|u, x')p(x' | u) dx' = \int p(x|u, x')p(x') dx'$$

In both case, we can remove the $u$ because the action gives no information on the prior state.

## Recursive Bayesian Filtering

### Context

Given:

- Alternation of actions $u$ and measurements/observations $z$: $d_t = {u_1, z_1, ..., u_t, y_t}$ ($d$ like data?)
- Sensor model: $P(x|z)$ (actual state given measurements)
- Action model: $P(x|u, x')$ (state given action was made and initial state)
- Prior probability of the system state: $P(x)$

Wanted:

- Estimate the state $x$ of a dynamical system
- Posterior of the state: **Belief**
  $$Bel(x_t) = P(x_t|u_1, z_1, ..., u_t, z_t)$$

### Markov (Independence) assumptions

We assume that $z_t$ is independent from all the measurements, actions and previous states if we know $x_t$.

### Bayes Filters
 
[Bayes Filters Demonstration](./bayes-filters-demo)

$y$ = observation, $x$ = state, $u$ = action

Definition:

$$Bel(x_t) = P(x_t|u_1, z_1, ..., u_t, z_t)$$

Bayes Filters Discrete case:
$$Bel(x_t) = \eta P(z_t| x_t) \Sigma_{x_{t-1}} P(x_t|u_t, x_{t-1}) Bel(x_{t-1})$$

Bayes Filter Continuous case:
$$Bel(x_t) = \eta P(z_t| x_t) \int P(x_t|u_t, x_{t-1}) Bel(x_{t-1}) dx_{t-1}$$

Finish part 3!!