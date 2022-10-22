import asyncio
import math
import time
from xml.etree.ElementTree import TreeBuilder
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()

    while True:
        for i in range(0, 1500):
            state = await c.set_position(position = math.nan, velocity = 0.01*i, maximum_torque = 1, query=True)
            print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
            print("Intended Velocity: ", 0.01*i)
            print()
            await asyncio.sleep(0.01)

        for i in reversed(range(0, 1500)):
            state = await c.set_position(position = math.nan, velocity = 0.01*i, maximum_torque = 1, query=True)
            print("Actual Velocity:", state.values[moteus.Register.VELOCITY])
            print("Intended Velocity: ", 0.01*i)
            print()
            await asyncio.sleep(0.01)     
           
if __name__ == '__main__':
    asyncio.run(main())