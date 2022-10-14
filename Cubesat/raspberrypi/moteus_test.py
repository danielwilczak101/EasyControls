import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    c.default_velocity_limit = 10

    await c.set_stop()

    while True:
        for i in range(9):
            await c.set_position(position = math.nan, velocity = i, maximum_torque = 1, query=True)
            await asyncio.sleep(0.1)

        await asyncio.sleep(0.001)


asyncio.run(main())   