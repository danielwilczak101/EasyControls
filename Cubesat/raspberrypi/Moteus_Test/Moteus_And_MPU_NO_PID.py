from this import d
import RPi.GPIO as GPIO
import time
from math import atan2, degrees
import board
import adafruit_mpu6050
import asyncio
import moteus

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_mpu6050.MPU6050(i2c)

async def main():
    c = moteus.Controller()

    await c.set_stop()

    while True:
        state = await c.set_position(position = math.nan, velocity = 0.1, maximum_torque = 1, query=True)
        print("Actual Velocity: ", state.values[moteus.Register.VELOCITY])
        print("Intended Velocity: ", 1)
        print()
        await asyncio.sleep(0.01)
  
if __name__ == '__main__':
    asyncio.run(main())