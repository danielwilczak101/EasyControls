import asyncio
import csv
import random
import serial

from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Iterator

from sympy import *
from sympy.utilities.lambdify import implemented_function

from smbus2 import SMBus

#Won't need this once new Pi hat is workingggggg
bus = SMBus(1)
# enter ls /dev/tty* into terminal to know what your Serial device name is, baud rate, timeout for read operations
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
# This will flush any byte that could already be in the input buffer at that point
ser.reset_input_buffer()

"""
FILENAME = Path("gyro.csv")
FIELDNAMES = ["x", "y", "z", "vx", "vy", "vz"]

if not FILENAME.exists():
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({name: name for name in FIELDNAMES})

async def gyroData():
    async with read_data() as data:
        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            while True:
                writer.writerow(dict(zip(FIELDNAMES, data)))
                await asyncio.sleep(0.1)

asyncio.run(gyroData())
"""
t,tau = symbols('t tau')
#These are guesstimates, need to acutally calculate
m = 4
r = 0.2
#Honestly no idea what these values should be, test n guess... message drakunov but also lookup
kp = 1.2
ki = .5
kd = .2
#Target is the value it should be steady at, can change to 30 deg, 99, -64, or whatever
target = 0
I = (m*r**2)/4

#ALL OF THIS CODE BESIDES THE SLIDING/PID CONTROLLER IS JACKS! THANK YOU MOFO 
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

start = datetime.now()

async def _read_until_stopped(data: list[float], stop: asyncio.Event) -> None:
    """Asynchronously updates data forever in the background."""
    while not stop.is_set():
        #print(ser.in_waiting)
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            #print(line)
            try:
                # Attempt to update the xyz.
                y, x, z = [float(x.strip())
                            for x in line.strip("[]").split(",")]
            except ValueError:
                print(line)
            else:
                start = datetime.now()
                if len(data) == 0:
                    data[:] = [x, y, z, 0.0, 0.0, 0.0]
                else:
                    dt = (datetime.now() - start).total_seconds()
                    start = datetime.now()
                    data[3] += ((x - data[0]) / dt - data[3]) / 5
                    data[4] += ((y - data[1]) / dt - data[4]) / 5
                    data[5] += ((z - data[2]) / dt - data[5]) / 5
                    data[0] = x
                    data[1] = y
                    data[2] = z
        # Let other code run asynchronously.
        await asyncio.sleep(0.01)


@asynccontextmanager
async def read_data() -> list[float]:
    data = []
    stop = asyncio.Event()
    stop.clear()
    task = asyncio.create_task(_read_until_stopped(data, stop))
    # Wait until data is filled with data.
    while len(data) == 0:
        await asyncio.sleep(0.1)
    try:
        # Let other code access the data values.
        yield data
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


async def go_crazy(duration: float) -> None:
    end_time = datetime.now() + timedelta(seconds=duration)
    for open_time, close_time in zip(random_generator(0.5, 2), random_generator(0.1, 0.5)):
        await random.choice([up_x, down_x])(open_time)
        await asyncio.sleep(close_time)
        if datetime.now() > end_time:
            break

#My codddeeeee
#x=read_data[3], ax=read_data[3] // input this unto function, poossibly calling outside of function to print error, or try to input "async with read_data() as data, Thruster.close_all():" "
async def main():
    end_time = datetime.now() + timedelta(seconds=55)
    await go_crazy(3)
    await asyncio.sleep(1)
    try:
        #print('pos data,time,error')
        async with read_data() as data, Thruster.close_all():
            print('pos data,time,error')
            while True:
                x = data[0]
                to = (datetime.now() - start).total_seconds()
                
                vx = data[3]
                ax = vx/to

                e = target - x
                p = implemented_function('p', lambda t: integrate((kp*e),(t,0,to)))
                i = implemented_function('i', lambda t, tau: integrate((ki*e),(tau, 0, (I*ax),(t, 0, (to)))))
                lam_p = lambdify(t, p(t))
                lam_i = lambdify([t,tau], i(t,tau))
                s = (lam_p(t) - lam_i(t,tau) - kd*e)
                u = sign(s)
                if u == 1:
                    await down_x(0.01)
                    await asyncio.sleep(0.1)
                elif u == -1:
                    await up_x(0.01)
                    await asyncio.sleep(0.1)
                if datetime.now() > end_time:
                    return
                print(x,',',to,',',e,flush=True)
    except OSError as e: #No idea what is, prolly lookup
        print(e)

asyncio.run(main())
    
'''
ORIGINAL CODE:
		if vx > 70 and abs(x) > 20:
                    await down_x(0.1)
                    await asyncio.sleep(0.1)
                elif vx < -70 and abs(x) > 20:
                    await up_x(0.1)
                    await asyncio.sleep(0.1)
                elif x > 5:
                    await down_x(min(0.25, x / 400))
                    await asyncio.sleep(abs(x) / 400)
                elif x < -5:
                    await up_x(min(0.25, -x / 400))
                    await asyncio.sleep(abs(x) / 400)
                else:
                    await asyncio.gather(*[
                        thruster.close(solinoid.name)
                        for thruster in Thruster
                        for solinoid in Solinoid
                    ])
                    await asyncio.sleep(abs(x) / 400)
'''