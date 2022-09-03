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

    async def impulse(self, solinoid):
        """Fires the solinoid as quick as possible."""
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

    @staticmethod
    @asynccontextmanager
    async def close_all():
        global bus
        try:
            yield
        finally:
            for _ in range(5):
                try:
                    await asyncio.gather(*[
                        thruster.close(solinoid.name)
                        for thruster in Thruster
                        for solinoid in Solinoid
                    ])
                except OSError as e:
                    bus = SMBus(1)
                    print(e)
                    await asyncio.sleep(1)
                else:
                    break


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
        await asyncio.sleep(0.01)


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


async def main():
    print("hello")
    async with read_data() as xyz:
        print("inside")
        for _ in range(10):
            print(xyz)
            await asyncio.sleep(1)

asyncio.run(main())
