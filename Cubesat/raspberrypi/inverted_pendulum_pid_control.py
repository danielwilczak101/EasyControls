#Goal: Implement a PID control system to appropriately accelerate reaction wheel to make the pendulum stand upright

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

#PID parameters

angle_increment = 0.0001
Imax = 50

Kp = -.5
Ki = .5 * 10^(-8)

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
    return vector_2_degrees(x,z), vector_2_degrees(y, z)


async def main():
    c = moteus.Controller()

    desiredAngle = 0

    await c.set_stop()

    while True:
        angle_xz, angle_yz = get_inclination(sensor)
        complementaryAngle = angle_yz - 90

        #Computing the error
        error = desiredAngle - complementaryAngle

        #Dithering
        if (error < 0):
            desiredAngle -= angle_increment
        else:
            desiredAngle += angle_increment

        #Integrate Error
        error_accumulation += error

        #Clamp the integrated error
        if error_accumulation > Imax:
            error_accumulation = Imax
        if error_accumulation < -Imax:
            error_accumulation = -Imax

        #Approx rate of change of error
        #error_deriv = (error - prev_error)

        #Velocity of wheel
        velocityOfReactionWheel = (Kp * error) + (Ki * error_accumulation) #+ (Kd * error_deriv)

       # prev_error = error

        await asyncio.sleep(0.01)

        state = await c.set_position(position = math.nan, velocity = velocityOfReactionWheel, maximum_torque = 60, accel_limit = 300, query = True)
        print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
        print("Angle: ", complementaryAngle)
        print()
        await asyncio.sleep(0.01)

if __name__ == '__main__':
    asyncio.run(main())
