# Week 4 - Proximity sensors

[Week 3.1](../w3/conditional-probability.md) | [Week 3.2](../w3/wheeled-locomotion.md) | [Mobile Robotics](../mobileRobotics.md) | [Week 5](../w5/probabilistic-robotics.md)

They are two kinds of distance sensors:
- **active** sensors
  - ultrasound 
  - laser
  - infrared 
- **passive** sensors
  - camera
  - tactile -> bumpers, touch sensors

## ultrasound

- ToF (Time of Flight)
- the larger the emitter, the better the angular resolution)
- bad resolution, crosstalk
- the speed of sound can be too slow for some applications
- you need many sensors to cover 360 deg

## laser

- ToF
- very precise
- fast
- wide field of view (one Lidar allows to scan 360 degrees)

## camera

- use two cameras to get depth measurements