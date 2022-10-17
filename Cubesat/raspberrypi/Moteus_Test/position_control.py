import asyncio
import math
import time
from xml.etree.ElementTree import TreeBuilder
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()


    for i in range(0, 4, 0.5):
        state = await c.set_position(position = i, maximum_torque = 1, query=True)
        print("Position: ", i)
        print()
        time.sleep(1)
        #await asyncio.sleep(1)
           
if __name__ == '__main__':
    asyncio.run(main())