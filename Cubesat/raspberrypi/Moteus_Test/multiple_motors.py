import asyncio
import math
import time
import moteus

async def main():
    transport = moteus.Fdcanusb()
    c1 = moteus.Controller(id = 1)
    c2 = moteus.Controller(id = 2)

    await c1.set_stop()
    await c2.set_stop()

    while True:
        print(await transport.cycle([
          c1.set_position(position = math.nan, velocity = 0.1, maximum_torque = 1, query=True),
          c2.set_position(position = math.nan, velocity = 0.1, maximum_torque = 1, query=True),
          asyncio.sleep(0.01)
        ]))
    # while True:
    #     state = await c.set_position(position = math.nan, velocity = 0.1, maximum_torque = 1, query=True)
    #     print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
    #     print("Intended Velocity: ", 1)
    #     print()
    #     await asyncio.sleep(0.01)
  
if __name__ == '__main__':
    asyncio.run(main())