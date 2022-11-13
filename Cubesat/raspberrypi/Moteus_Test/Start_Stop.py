import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()

    while True:
        for x in range(500):
            state = await c.set_position(position = math.nan, velocity = x/10, maximum_torque = 1, query=True)
            print("X: ", x)
            print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
            print("Intended Velocity: ", x/10)
            print()
            await asyncio.sleep(0.01)
        for x in range(100):
            state = await c.set_position(position = math.nan, velocity = 0, maximum_torque = 5, query=True)
            print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
            print("Intended Velocity: 0")
            print()
            await asyncio.sleep(0.01)
  
if __name__ == '__main__':
    asyncio.run(main())