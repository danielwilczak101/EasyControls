import asyncio
import math
import time
import moteus

c = moteus.Controller()

c.set_position(.5)

""" async def main():
    c = moteus.Controller()

    while True:
            print(await c.set_position(.5, query=True))
            await asyncio.sleep(0.001)



asyncio.run(main())    """     