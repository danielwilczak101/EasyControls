import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()
    targetVelocity = 0.1

    await c.set_stop()

    while True:
        state = await c.set_position(position = math.nan, velocity = targetVelocity, maximum_torque = 1, query=True)
        print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
        print("Intended Velocity: ", targetVelocity)
        print()
        await asyncio.sleep(0.01)
  
if __name__ == '__main__':
    asyncio.run(main())