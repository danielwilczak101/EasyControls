import asyncio
import csv
import random
import serial

from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Iterator

from smbus import SMBus

bus = SMBus(1)
# enter ls /dev/tty* into terminal to know what your Serial device name is, baud rate, timeout for read operations
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
# This will flush any byte that could already be in the input buffer at that point
ser.reset_input_buffer()

"""
FILENAME = Path("gyro.csv")

if not FILENAME.exists():
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["x", "y", "z"])
        writer.writerow({"x": "x", "y": "y", "z": "z"})

async def gyroData():
    async with read_data() as xyz:
        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["x", "y", "z"])
            while True:
                writer.writerow({"x": xyz[0], "y": xyz[1], "z": xyz[2]})
                await asyncio.sleep(0.1)

asyncio.run(gyroData())
"""

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
        self.is_open = [False, False]

    async def impulse(self, solinoid):
        """Fires the solinoid as quick as possible."""
        value = Solinoid[solinoid.upper()].value
        if self.is_open[value]:
            await self.close()
        else:
            self.is_open[value] = True
            bus.write_byte_data(self.address, value, 2)
            self.is_open[value] = False
            await asyncio.sleep(0.1)

    async def open(self, solinoid, duration=None):
        """Leaves solinoid open indefinedtly untill otherwise closed"""
        value = Solinoid[solinoid.upper()].value
        if not self.is_open[value]:
            self.is_open[value] = True
            try:
                bus.write_byte_data(self.address, value, 1)
            except OSError:
                self.is_open[value] = False
                raise
            if duration is None:
                await asyncio.sleep(0.1)
            else:
                await asyncio.sleep(max(0.1, duration))
                await self.close(solinoid)

    async def close(self, solinoid):
        """Leaves solinoid closed indefinedtly untill otherwise opened"""
        value = Solinoid[solinoid.upper()].value
        if self.is_open[value]:
            self.is_open[value] = False
            try:
                bus.write_byte_data(self.address, value, 0)
            except OSError:
                self.is_open[value] = True
            await asyncio.sleep(0.1)

    @staticmethod
    @asynccontextmanager
    async def close_all():
        try:
            yield
        finally:
            await asyncio.sleep(0.1)
            try:
                for thruster in Thruster:
                    for solinoid in Solinoid:
                        bus.write_byte_data(
                            thruster.address, solinoid.value, 0)
                        thruster.is_open[solinoid.value] = False
            except OSError as e:
                print(e)
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


async def up_x(duration=None):
    await asyncio.gather(
        Thruster.TWO.close("bottom"),
        Thruster.SIX.close("bottom"),
        Thruster.FIVE.close("top"),
        Thruster.THREE.close("top"),
    )
    await asyncio.gather(
        Thruster.TWO.open("top", duration),
        Thruster.SIX.open("top", duration),
        Thruster.FIVE.open("bottom", duration),
        Thruster.THREE.open("bottom", duration),
    )


async def down_x(duration=None):
    await asyncio.gather(
        Thruster.TWO.close("top"),
        Thruster.SIX.close("top"),
        Thruster.FIVE.close("bottom"),
        Thruster.THREE.close("bottom"),
    )
    await asyncio.gather(
        Thruster.TWO.open("bottom", duration),
        Thruster.SIX.open("bottom", duration),
        Thruster.FIVE.open("top", duration),
        Thruster.THREE.open("top", duration),
    )

def random_generator(lower: float, upper: float) -> Iterator[float]:
    return (random.uniform(lower, upper) for _ in iter(int, None))

async def go_crazy(thruster: Thruster, solinoid: str, duration: float) -> None:
    end_time = datetime.now() + timedelta(seconds=duration)
    for open_time, close_time in zip(random_generate(0.1, 0.5), random_generator(0.1, 0.5)):
        await thruster.open(solinoid, open_time)
        await thruster.close(solinoid)
        await asyncio.sleep(close_time)
        if datetime.now() > end_time:
            break

async def go_all_crazy(duration: float) -> None:
    async with Thruster.close_all():
        await asyncio.gather(*[
            go_crazy(thruster, solinoid.name.lower(), duration)
            for thurster in Thruster
            for solinoid in Solinoid
        ])

async def main():
    await go_all_crazy(5)
    await asyncio.sleep(1)
    while True:
        try:
            async with read_data() as xyz, Thruster.close_all():
                while True:
                    if xyz[0] > 5:
                        await down_x(min(0.25, xyz[0] / 200))
                    elif xyz[0] < -5:
                        await up_x(min(0.25, -xyz[0] / 200))
                    else:
                        await asyncio.gather(*[
                            thruster.close(solinoid.name)
                            for thruster in Thruster
                            for solinoid in Solinoid
                        ])
        except OSError as e:
            print(e)

asyncio.run(main())
