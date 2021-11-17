### Problem
Doesnt use acceleration vector to compinsate for drift.  
Had a wierd problem with gravity working on one side of an axis but not on the other.  
  - Ex. ~1 on one side of x axis and 0.4 on the other side of the same axis.

### Update
Updated code so that it now integrates the gyroscope data and uses the bias to remove the initial error.

### Package information
https://pypi.org/project/mpu9250-jmdev/#How-To-Use

### Current code.
In file.

## Wiring
3.3 - VCC  
GND - GND  
SCL - SCL  
SDA - SDA  
