#Goal: Implement a PID control system to appropriately accelerate reaction wheel to make the pendulum stand upright

import time
#from math import atan2, degrees
import math
import asyncio
import moteus



c = moteus.Controller()


#PID parameters

angle_increment = 0.0001
Imax = 50

Kp = 1.75
Ki = 1 * 10**(-5)
Kd = 0 * 10**4

# Given a point (x, y) return the angle of that point relative to x axis.
# Returns: angle in degrees




# Given an accelerometer sensor object return the inclination angles of X/Z and Y/Z
# Returns: tuple containing the two angles in degrees





async def main():
    desiredAngle = 0
    error_accumulation = 0
    prev_error = 0

    await c.set_stop()

    while True:

        state = await c.set_position(position = math.nan, velocity = 10, maximum_torque = 100, accel_limit = math.nan, query = True)
        print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
        print()
        await asyncio.sleep(0.01)

if __name__ == '__main__':
    asyncio.run(main())
