import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()

    await c.set_position(.99, 1, .1, query=True)

    await asyncio.sleep(0.001)


asyncio.run(main())   