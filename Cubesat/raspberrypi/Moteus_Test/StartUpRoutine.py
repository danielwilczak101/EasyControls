#Authur: Justin Hartland
#Purpose: To implement a PID controller to achieve CubeSat 1DoF stability

import asyncio
import time
import math
from math import atan2, degrees
import moteus

async def main():
    c = moteus.Controller()
    await c.set_stop()

    for x in range(5000):
        state = await c.set_position(position = math.nan, velocity = 100, accel_limit = 200, query=True)


    await c.set_stop()
    #state = await c.set_position(position = math.nan, velocity = 100, accel_limit = 200, query=True)

    await asyncio.sleep(0.01)



if __name__ == '__main__':
    asyncio.run(main())