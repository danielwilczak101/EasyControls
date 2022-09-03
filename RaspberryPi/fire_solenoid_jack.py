from smbus import SMBus
from time import sleep
from enum import Enum
import asyncio
from contextlib import asynccontextmanager
import serial

bus = SMBus(1)
# enter ls /dev/tty* into terminal to know what your Serial device name is, baud rate, timeout for read operations
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
# This will flush any byte that could already be in the input buffer at that point
ser.reset_input_buffer()


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

    def __init__(self, address) -> None:
        self.address = address
        self.is_open = False

    async def impulse(self, solinoid):
        """Fires the solinoid as quick as possible."""
        if self.is_open:
            await self.close()
        else:
            self.is_open = True
            bus.write_byte_data(
                self.address, Solinoid[solinoid.upper()].value, 2)
            self.is_open = False
            await asyncio.sleep(0.1)

    async def open(self, solinoid):
        """Leaves solinoid open indefinedtly untill otherwise closed"""
        if not self.is_open:
            self.is_open = True
            try:
                bus.write_byte_data(
                    self.address, Solinoid[solinoid.upper()].value, 1)
            except OSError:
                self.is_open = False
                raise
            await asyncio.sleep(0.1)

    async def close(self, solinoid):
        """Leaves solinoid closed indefinedtly untill otherwise opened"""
        if self.is_open:
            self.is_open = False
            try:
                bus.write_byte_data(
                    self.address, Solinoid[solinoid.upper()].value, 0)
            except OSError:
                self.is_open = True
            await asyncio.sleep(0.1)

    @staticmethod
    @asynccontextmanager
    async def close_all():
        global bus
        try:
            yield
        except OSError:
            await asyncio.sleep(5)
            bus = SMBus(1)
            raise
        finally:
            try:
                await asyncio.gather(*[
                    thruster.close(solinoid.name)
                    for thruster in Thruster
                    for solinoid in Solinoid
                ])
            except OSError:
                pass


async def _read_until_stopped(xyz: list[float], stop: asyncio.Event) -> None:
    """Asynchronously updates xyz forever in the background."""
    while not stop.is_set():
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            try:
                # Attempt to update the xyz.
                data = [float(x.strip()) for x in line.strip("[]").split(",")]
                x = data[1]
                y = data[0]
                z = data[2]
                xyz[:] = [x, y, z]
            except ValueError:
                print(line)
        # Let other code run asynchronously.
        await asyncio.sleep(0)


@asynccontextmanager
async def read_data() -> list[float]:
    xyz = []
    stop = asyncio.Event()
    stop.clear()
    task = asyncio.create_task(_read_until_stopped(xyz, stop))
    # Wait until xyz is filled with data.
    while len(xyz) == 0:
        await asyncio.sleep(0)
    try:
        # Let other code access the xyz values.
        yield xyz
    finally:
        # Stop reading data.
        stop.set()
        await task


async def up_x():
    await asyncio.gather(
        Thruster.TWO.close("bottom"),
        Thruster.SIX.close("bottom"),
        Thruster.FIVE.close("top"),
        Thruster.THREE.close("top"),
    )
    await asyncio.gather(
        Thruster.TWO.open("top"),
        Thruster.SIX.open("top"),
        Thruster.FIVE.open("bottom"),
        Thruster.THREE.open("bottom"),
    )


async def down_x():
    await asyncio.gather(
        Thruster.TWO.close("top"),
        Thruster.SIX.close("top"),
        Thruster.FIVE.close("bottom"),
        Thruster.THREE.close("bottom"),
    )
    await asyncio.gather(
        Thruster.TWO.open("bottom"),
        Thruster.SIX.open("bottom"),
        Thruster.FIVE.open("top"),
        Thruster.THREE.open("top"),
    )


async def main():
    async with read_data() as xyz, Thruster.close_all():
        while True:
            if xyz[0] > 20:
                await down_x()
            elif xyz[0] < -20:
                await up_x()
            else:
                async with Thruster.close_all():
                    pass

asyncio.run(main())
