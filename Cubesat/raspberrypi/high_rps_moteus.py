import asyncio
import math
import time
from xml.etree.ElementTree import TreeBuilder
import moteus

async def main():
    c = moteus.Controller()

    c.deafult_velocity_limit = 30

    await c.set_stop()

    while True:
        for i in range(0, 4000):
            state = await c.set_position(position = math.nan, velocity = i*0.01, maximum_torque = 1, query=True)
            print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
            print("Intended Velocity: ", 0.01*i)
            print()
            await asyncio.sleep(0.01)

 
           
if __name__ == '__main__':
    asyncio.run(main())