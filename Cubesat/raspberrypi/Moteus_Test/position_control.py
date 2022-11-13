import asyncio
import math
import time
#from xml.etree.ElementTree import TreeBuilder
import moteus

async def main():
    c = moteus.Controller()

    for x in range(2000):
        print(await c.seet_position(position=0.9*math.sin(math.pi*x/500), query = True))
        await asyncio.sleep(0.001)
    
    print (await c.set_stop(query = True))

           
asyncio.run(main())