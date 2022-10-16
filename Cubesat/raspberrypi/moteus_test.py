import asyncio
import math
import time
from xml.etree.ElementTree import TreeBuilder
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()
    
    for i in range(500):
        await c.set_position(position = math.nan, velocity = 0.01*i, maximum_torque = 1, query=True)
        print(0.01*i)
        await asyncio.sleep(0.01)

    for i in reversed(range(500)):
        await c.set_position(position = math.nan, velocity = 0.01*i, maximum_torque = 1, query=True)
        print(0.01*i)
        await asyncio.sleep(0.01)     
           
  

asyncio.run(main())   