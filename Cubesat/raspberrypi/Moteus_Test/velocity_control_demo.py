import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()

    while True:
        state = await c.set_position(position = math.nan, velocity = 10, maximum_torque = 1, query=True)
        print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
        print("Intended Velocity: ", 10)
        print()
        await asyncio.sleep(0.01)
  
if __name__ == '__main__':
    asyncio.run(main())