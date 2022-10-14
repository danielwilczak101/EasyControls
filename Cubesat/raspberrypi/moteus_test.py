import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()

    while True:
        await c.set_position(position = math.nan, velocity = 50, maximum_torque = 1, query=True)
        await asyncio.sleep(0.01)




asyncio.run(main())   