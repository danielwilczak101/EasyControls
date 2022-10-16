import asyncio
import math
import time
from xml.etree.ElementTree import TreeBuilder
import moteus

async def main():
    c = moteus.Controller()

    c.max_velocity = math.nan

    await c.set_stop()
    while True:
        for i in range(2500, 3500):
            state = await c.set_position(position = math.nan, velocity = 0.01*i + 1, maximum_torque = 1, query=True)
            print("Velocity:", state.values[moteus.Register.VELOCITY])
            print()
            print(0.01*i + 1)
            await asyncio.sleep(0.01)

        for i in reversed(range(2500, 3500)):
            state = await c.set_position(position = math.nan, velocity = 0.01*i + 1, maximum_torque = 1, query=True)
            print("Velocity:", state.values[moteus.Register.VELOCITY])
            print()
            print(0.01*i + 1)
            await asyncio.sleep(0.01)     
           
  
if __name__ == '__main__':
    asyncio.run(main())