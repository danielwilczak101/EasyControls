import asyncio
import math
import time
from xml.etree.ElementTree import TreeBuilder
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()
    while True:
        for i in range(5000):
            await c.set_position(position = math.nan, velocity = 0.01*i + 1, maximum_torque = 10, query=True)
            print(0.01*i)
            await asyncio.sleep(0.005)

        for i in reversed(range(5000)):
            await c.set_position(position = math.nan, velocity = 0.01*i + 1, maximum_torque = 10, query=True)
            print(0.01*i)
            await asyncio.sleep(0.005)     
           
  

asyncio.run(main())   