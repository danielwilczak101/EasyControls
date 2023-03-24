#Authur: Justin Hartland
#Purpose: To implement a PID controller to achieve CubeSat 1DoF stability

import asyncio
import time
import math
import board
import adafruit_mpu6050
import moteus
import moteus_pi3hat
        

async def main():
    c = moteus.Controller()
    transport = moteus_pi3hat.Pi3HatRouter()
    await c.set_stop()

    Kp = -1
    Ki = 1
    Kd = 1

    desiredAngleRange = 10
    desiredAngle = 0

    while True:
        result = await transport.cycle([], request_attitude=True)
        imu_result = [
            x for x in result
            if x.id == -1 and isinstance(x, moteus_pi3hat.CanAttitudeWrapper)][0]
        
        cubeSatAngle = euler_rad.pitch * (180/math.pi)

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