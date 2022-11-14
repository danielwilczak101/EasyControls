#The purpose of this code is to spin the motor up to 50 rps and then instantly stop the motor from rotating
#No success yet

import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()

    c.max_position_slip = 10

    await c.set_stop()

    while True:
        for x in range(500):
            state = await c.set_position(position = math.nan, velocity = 40, maximum_torque = 1, query=True)
            print("X: ", x)
            print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
            print("Intended Velocity: ", 40)
            print()
            await asyncio.sleep(0.01)

        for x in range(500):
            state = await c.set_position(position = math.nan, velocity = -40, maximum_torque = 1, query=True)
            print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
            print("Intended Velocity: 40")
            print()
            await asyncio.sleep(0.01)
  
if __name__ == '__main__':
    asyncio.run(main())