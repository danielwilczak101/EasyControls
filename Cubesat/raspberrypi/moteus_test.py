import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    while True:
        for i in range(99):
            print(await c.set_position(i/100, query=True))
        for i in range(99,0):
            print(await c.set_position(i/100, query=True))

        await asyncio.sleep(0.001)



asyncio.run(main())   