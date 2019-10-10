# Week 2 - Robot control paradigms

[Home](../../../../README.md) | [Mobile Robotics](../mobileRobotics.md)

- In the 70ies: **Sense -> Plan -> Act**, repeat

  - **hierarchical** or **deliberative** paradigm
  - "perfect world" -> you know exactly where everything is (doesn't change) and use this knowledge to decide what the next step is
  - considering that you have perfect sensors
  - very rigid, maybe the planning phase not necessary at all?
  - you cannot react to quick changes, **sequential**

- In the 80ies: **Sense <-> Act**

  - **reactive** or **behavior based** paradigm
  - no model
  - "competing desires": avoid obstacles, explore, move around
  - no memory
  - only behavior-specific sensing (-> info with direct influence on the behavior)
  - modules are grouped in layers that each have a specific function (like said previously: wander, explore, avoid), some of the layers can be incorporated to others (?)
  - emergent overall behavior
  - treat the robot as a **particle in a potential field**: the robot moves according to a sum of forces defined by the programmer -> swarm robotics
    - tangential forces: to turn around an object
    - uniform force: to move along a corridor
    - to have a robot that is wandering, get a repulsive force and a uniform force
    - **beware: local minima!** (U-shaped obstacles) -> you can introduce random motion to escape them
    - easy to calculate (fast!)
    - requires high refresh rate
    - hard to tune
    - this method can be used for a vacuum cleaner!

- **Hybrid** deliberative/reactive paradigm: **Sense <-> Act and sometimes Plan**
  - some people wanted to mix the two previous approaches
  - you directly react to the environment in general, but a higher level still has a specific goal and plans how to achieve it the best
