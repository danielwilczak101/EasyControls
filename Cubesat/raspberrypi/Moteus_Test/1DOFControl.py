#Authur: Justin Hartland
#Purpose: To implement a PID controller to achieve CubeSat 1DoF stability

import asyncio
import time
import math
from math import atan2, degrees
import board
import adafruit_mpu6050
import moteus
import matplotlib.pyplot as plt

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_mpu6050.MPU6050(i2c)

# Given a point (x, y) return the angle of that point relative to x axis.
# Returns: angle in degrees

def vector_2_degrees(flag, initialAngle, x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle = angle +360
    if flag == 1:
        initialAngle = angle
        flag = 0
    if angle <= initialAngle:
        angle = -1* (angle - initialAngle)
    else:
        angle = abs(angle - 360) + initialAngle
    return angle, flag, initialAngle

# Given an accelerometer sensor object return the inclination angles of X/Z and Y/Z
# Returns: tuple containing the two angles in degrees

def get_inclination(flag, initialAngle, _sensor):
    x, y, z = _sensor.acceleration
    return vector_2_degrees(flag, initialAngle, y, z)

def getAngle(flag, initialAngle):
    angleOfCubeSat, flag, initialAngle = get_inclination(flag, initialAngle, sensor)
    return angleOfCubeSat, flag, initialAngle
        

async def main():
    c = moteus.Controller()
    await c.set_stop()

    flag = 1
    initialAngle = 0
    angleList = []

    Kp = -1
    Ki = 1
    Kd = 1

    desiredAngleRange = 10
    desiredAngle = 206

    while True:
        cubeSatAngle, flag, initialAngle = getAngle(flag, initialAngle)

        error = (desiredAngle - cubeSatAngle)

        if abs(error) < desiredAngle/2:
            error = 0
        elif error < 0:
            error = ((desiredAngle + desiredAngleRange/2) - cubeSatAngle)
        elif error > 0:
            error = ((desiredAngle - desiredAngleRange/2) - cubeSatAngle)

        motorVelocity = Kp * error

        state = await c.set_position(position = math.nan, velocity = motorVelocity, accel_limit = 100, query=True)
        await asyncio.sleep(0.01)



if __name__ == '__main__':
    asyncio.run(main())