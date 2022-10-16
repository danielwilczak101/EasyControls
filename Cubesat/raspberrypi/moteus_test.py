import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()


    await c.set_position(position = math.nan, velocity = 10, maximum_torque = 1, query=True)
    
"""     while True:
        await c.set_position(position = math.nan, velocity = 10, maximum_torque = 1, query=True)
        await asyncio.sleep(0.01) """

"""         await c.set_position(position = math.nan, velocity = 5, maximum_torque = 1, query=True)
        await asyncio.sleep(0.1)
        await c.set_position(position = math.nan, velocity = 10, maximum_torque = 1, query=True)
        await asyncio.sleep(0.1) """
  

asyncio.run(main())   