#Authur: Justin Hartland
#Purpose: To implement a PID controller to achieve CubeSat 1DoF stability

import asyncio
import time
from math import atan2, degrees
import board
import adafruit_mpu6050
import moteus

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_mpu6050.MPU6050(i2c)

# Given a point (x, y) return the angle of that point relative to x axis.
# Returns: angle in degrees

def vector_2_degrees(flag, x, y):
    angle = degrees(atan2(y, x))
    if flag == 1:
        initialAngle = angle
        flag = 0
    angle = angle - initialAngle
    return angle, flag

# Given an accelerometer sensor object return the inclination angles of X/Z and Y/Z
# Returns: tuple containing the two angles in degrees

def get_inclination(flag, _sensor):
    x, y, z = _sensor.acceleration
    return vector_2_degrees(flag, y, z)

def getAngle(flag):
    angleOfCubeSat, flag = get_inclination(flag, sensor)
    print("YZ angle = {:6.2f}deg".format(
        angleOfCubeSat))
    return angleOfCubeSat, flag
        

async def main():
    c = moteus.Controller()
    await c.set_stop()

    flag = 1

    Kp = 0.1
    Ki = 1
    Kd = 1

    desiredAngleRange = 10
    desiredAngle = 180

    while True:
        cubeSatAngle, flag = getAngle(flag)
        error = (desiredAngle - cubeSatAngle)
        motorVelocity = Kp * error

        state = await c.set_position(velocity = motorVelocity, accel_limit = 100, query=True)
        await asyncio.sleep(0.01)



if __name__ == '__main__':
    asyncio.run(main())