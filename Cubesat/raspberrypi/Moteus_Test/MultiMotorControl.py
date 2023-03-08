import asyncio
import math
import moteus
import moteus_pi3hat
import time

async def main():
    transport = moteus_pi3hat.Pi3HatRouter(
        servo_bus_map = {
            1:[11],
        }
    )

    servos = {
        servo_id : moteus.Controller(id=servo_id, transport=transport)
        for servo_id in [11]
    }

    #Removes any fault states on controllers
    await transport.cycle([x.make_stop() for x in servos.values()])

    while True:
        now = time.time()

        commands = [
                servos[11].make_position(
                    position=math.nan,
                    velocity=0.1*math.sin(now),
                    query=True),
        ]

        await transport.cycle(commands)

        await asyncio.sleep(0.02)

if __name__ == '__main__':
    asyncio.run(main())
    
