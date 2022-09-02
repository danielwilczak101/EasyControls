from smbus import SMBus
from time import sleep
from enum import Enum
import asyncio


bus = SMBus(1)


class Solinoid(Enum):
    TOP = 0
    BOTTOM = 1


class Thruster(Enum):

    ONE = 0x10
    TWO = 0x11
    THREE = 0x12
    FOUR = 0x13
    FIVE = 0x14
    SIX = 0x15

    async def impulse(self, solinoid):
        """Fires the solinoid as quick as possible"""

        bus.write_byte_data(self.value, Solinoid[solinoid.upper()].value, 2)
        await asyncio.sleep(0.01)

    async def open(self, solinoid):
        """Leaves solinoid open indefinedtly untill otherwise closed"""
        bus.write_byte_data(self.value, Solinoid[solinoid.upper()].value, 1)
        await asyncio.sleep(0.01)

    async def close(self, solinoid):
        """Leaves solinoid closed indefinedtly untill otherwise opened"""
        bus.write_byte_data(self.value, Solinoid[solinoid.upper()].value, 0)
        await asyncio.sleep(0.01)

    async def close_all():
        await asyncio.gather(*[
            thruster.close(solinoid.name)
            for thruster in Thruster
            for solinoid in Solinoid
        ])


async def main():
    for _ in range(5):
        await asyncio.gather(
            Thruster.TWO.open("top"),
            Thruster.SIX.open("top"),
            Thruster.FIVE.open("bottom"),
            Thruster.THREE.open("bottom"),
        )

        asyncio.sleep(3)
        Thruster.close_all()

        await asyncio.gather(
            Thruster.TWO.open("bottom"),
            Thruster.SIX.open("botoom"),
            Thruster.FIVE.open("top"),
            Thruster.THREE.open("top"),
        )

        asyncio.sleep(3)
        Thruster.close_all()

asyncio.run(main())
