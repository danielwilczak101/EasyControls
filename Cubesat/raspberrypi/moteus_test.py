import asyncio
import math
import time
import moteus

c = moteus.Controller()

c.set_position(.5, query=True)
""" async def main():
    c = moteus.Controller()

    while True:

        for x in range(2000):
            print(await c.set_position(position=0.9*math.sin(math.pi*x/500), query=True))
            await asyncio.sleep(0.001)

        for x in range(2000, 0):
            print(await c.set_position(position=0.9*math.sin(math.pi*x/500), query=True))
            await asyncio.sleep(0.001)    

        print(await c.set_stop(query=True))



asyncio.run(main())         """