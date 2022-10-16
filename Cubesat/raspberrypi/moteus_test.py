import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()

    while True:
        for i in range (3):
            await c.set_position(position = math.nan, velocity = (i*5), maximum_torque = 1, query=True)
            await asyncio.sleep(2)

        for i in range (2,0):
            await c.set_position(position = math.nan, velocity = (i*5), maximum_torque = 1, query=True)
            await asyncio.sleep(2)    




asyncio.run(main())   