#Goal: Implement a simple negative feedback control system: if the angle of the pendulum is less than 0 degrees, then the reaction wheel rotates clockwise at a constant velocity and vice versa. 
#No PID implementation

import RPi.GPIO as GPIO
import time
#from math import atan2, degrees
import math
import board
import adafruit_mpu6050
import asyncio
import moteus

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_mpu6050.MPU6050(i2c)

# Given a point (x, y) return the angle of that point relative to x axis.
# Returns: angle in degrees


def vector_2_degrees(x, y):
    angle = math.degrees(math.atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


# Given an accelerometer sensor object return the inclination angles of X/Z and Y/Z
# Returns: tuple containing the two angles in degrees


def get_inclination(_sensor):
    x, y, z = _sensor.acceleration
    return vector_2_degrees(x, z), vector_2_degrees(y, z)


async def main():
    direction = 1
    c = moteus.Controller()

    await c.set_stop()

    while True:
        angleXZ, angleOfPendulum = get_inclination(sensor)
        
        if (angleOfPendulum - 90) <= 0:
            direction = 1
        else:
            direction = -1
        
        state = await c.set_position(position = math.nan, velocity = 0.1 * direction, maximum_torque = 1, query=True)
        print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
        print()
        await asyncio.sleep(0.01)
  
if __name__ == '__main__':
    asyncio.run(main())