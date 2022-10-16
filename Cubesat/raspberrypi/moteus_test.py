import asyncio
import math
import time
from xml.etree.ElementTree import TreeBuilder
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()
    
    while True:
        for i in range(1000):
            await c.set_position(position = math.nan, velocity = 0.01*i, maximum_torque = 5, query=True)
            await asyncio.sleep(0.01)
        for i in range(1000,0):
            await c.set_position(position = math.nan, velocity = 0.01*i, maximum_torque = 5, query=True)
            await asyncio.sleep(0.01)    
    

"""         await c.set_position(position = math.nan, velocity = 5, maximum_torque = 1, query=True)
        await asyncio.sleep(0.1)
        await c.set_position(position = math.nan, velocity = 10, maximum_torque = 1, query=True)
        await asyncio.sleep(0.1) """
  

asyncio.run(main())   