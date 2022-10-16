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
            await c.set_position(position = math.nan, velocity = 0.01*i + 1, maximum_torque = 1, query=True)
            print("Velocity:", state.values[c.Register.VELOCITY])
            await asyncio.sleep(0.01)

        for i in reversed(range(1000)):
            await c.set_position(position = math.nan, velocity = 0.01*i + 1, maximum_torque = 1, query=True)
            print("Velocity:", state.values[c.Register.VELOCITY])
            await asyncio.sleep(0.01)     
           
  

asyncio.run(main())   