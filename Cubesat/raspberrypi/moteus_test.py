import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()

    while True:
        await c.set_position(.5, query=True)

        await asyncio.sleep(0.001)


asyncio.run(main())   