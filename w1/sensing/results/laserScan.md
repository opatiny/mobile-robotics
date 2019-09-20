# Observations about polarLaserScan plot

We see that the measurements oscillate between 0 and some values that would form a continuous obstacle. It is as if there was a grid just in front of the sensor. Otherwise, if it is not hardware, it might be a problem with the sensor itself. Maybe it could not refresh quickly enough something, or it did saturate, or the light emmited didn't come back because of ambient light?

Solution: It seems that the laser sensor can sometimes see through the walls -> it can be the case if some obstacles are semi-transparent (glass, grid, ...)