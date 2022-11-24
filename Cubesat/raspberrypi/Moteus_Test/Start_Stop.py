#Goal of this code: To instantly accelerate motor to 75 rps, brake, then instantly accelerate to -75 rps, brake, and repeat
#Current State: Goal achieved
#Notes: All though I do not know why, the solution was changing the delay in the brake for loop to 0.02 seconds
 
import asyncio
import math
import time
import moteus

async def main():
    c = moteus.Controller()
    c.max_position_slip=1
    speed = 80
    direction = 1
    await c.set_stop()

    for x in range(4):
        for x in range(200):
            state = await c.set_position(position = math.nan, maximum_torque=60, velocity = speed * direction, accel_limit=300, query=True)
            print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
            print("Intended Velocity: ", speed*direction) 
            print()
            await asyncio.sleep(0.01)

<<<<<<< HEAD
        for x in range(100):
            c.make_brake()
            await asyncio.sleep(0.02)

        direction = direction * -1

        await c.set_stop()

    await c.set_stop()

=======
        for x in range(500):
            state = await c.set_position(position = math.nan, velocity = -40, maximum_torque = .5, query=True)
            print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
            print("Intended Velocity: 40")
            print()
            await asyncio.sleep(0.01)
  
>>>>>>> e340de4faf55245504c213ee2e87512e438ff85f
if __name__ == '__main__':
    asyncio.run(main())
