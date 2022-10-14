import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()

    while True:
        for i in range(10):
            await c.set_position(.5, 1, i/10, query=True)

        await asyncio.sleep(0.001)


asyncio.run(main())   