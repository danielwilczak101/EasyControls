import asyncio
import numpy as np
from datetime import datetime, timedelta
from enum import Enum
from sympy import symbols, integrate, lambdify, sign
from smbus2 import SMBus
from adafruit_bno055 import BNO055_I2C
from board import SCL, SDA
from busio import I2C
from contextlib import asynccontextmanager


import sqlite3

database = 'imu_data.db'

def init_db():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # Create table with an auto-incrementing ID
    c.execute('''CREATE TABLE IF NOT EXISTS imu_data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp TEXT, roll REAL, pitch REAL, yaw REAL, 
                  quat_i REAL, quat_j REAL, quat_k REAL, 
                  angular_velocity_x REAL, angular_velocity_y REAL, angular_velocity_z REAL, 
                  angular_acceleration_x REAL, angular_acceleration_y REAL, angular_acceleration_z REAL)''')
    # New table for control variables
    c.execute('''CREATE TABLE IF NOT EXISTS control_log
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp TEXT, error REAL, control_variable REAL, control_action INTEGER)''')
    conn.commit()
    conn.close()
   
init_db()  # Initialize the database and table

# Initialize the SMBus for the solenoids control
bus = SMBus(1)

# Setup for BNO055 sensor
i2c = I2C(SCL, SDA)
sensor = BNO055_I2C(i2c)

# Constants and variables
t, l = symbols('t l')
m = 4
r = 0.2
kp = .7
ki = .5
kd = 1
target = 60
I = (m * r**2) / 4

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

    async def open(self, solinoid, duration=None):
        value = solinoid.value
        if not self.is_open[value]:
            self.is_open[value] = True
            try:
                bus.write_byte_data(self.address, value, 1)
                if duration:
                    await asyncio.sleep(duration)
                    await self.close(solinoid)
            except OSError:
                self.is_open[value] = False
                raise

    
    async def close(self, solinoid):
        value = solinoid.value
        self.is_open[value] = False
        bus.write_byte_data(self.address, value, 0)
        await asyncio.sleep(0.05)

@asynccontextmanager
async def close_all():
    try:
        yield
    finally:
        await asyncio.sleep(0.1)
        for thruster in Thruster:
            for solinoid in Solinoid:
                bus.write_byte_data(thruster.value, solinoid.value, 0)
                thruster.is_open[solinoid.value] = False

async def up_x(duration=None):
    await asyncio.gather(
        Thruster.TWO.open(Solinoid.BOTTOM, duration),
        Thruster.SIX.open(Solinoid.BOTTOM, duration),
        Thruster.FIVE.open(Solinoid.TOP, duration),
        Thruster.THREE.open(Solinoid.TOP, duration),
    )

async def down_x(duration=None):
    await asyncio.gather(
        Thruster.TWO.open(Solinoid.TOP, duration),
        Thruster.SIX.open(Solinoid.TOP, duration),
        Thruster.FIVE.open(Solinoid.BOTTOM, duration),
        Thruster.THREE.open(Solinoid.BOTTOM, duration),
    )


async def read_imu_data(stop: asyncio.Event, data: list):
    last_time = datetime.now()
    last_gyro = np.array(sensor.gyro)

    #Open Connection to Database
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
    except Exception as e:
        print(f"Database connection error: {e}")
        return


    while not stop.is_set():
        quat = sensor.quaternion
        gyro = np.array(sensor.gyro)
        euler = sensor.euler  # Euler angles

        # Convert gyro from radians per second to degrees per second
        gyro_deg_s = gyro * (180 / np.pi)

        if quat is not None and gyro is not None:
            current_time = datetime.now()
            dt = (current_time - last_time).total_seconds()
            angular_acceleration = (gyro_deg_s - last_gyro) / dt if dt > 0 else np.array([0.0, 0.0, 0.0])

            #data[:] = [quat[1], quat[2], quat[3], gyro[0], gyro[1], gyro[2], angular_acceleration[0], angular_acceleration[1], angular_acceleration[2]]

            # Map Euler angles from -180 to 180, to 0 to 360
            #mapped_euler = np.mod(np.array(euler) + 360, 360)

            # Update the data list to include Euler angles
            # Now data contains: Euler angles, quaternion, angular velocity, angular acceleration
            data[:] = [euler[0], euler[1], euler[2], quat[1], quat[2], quat[3], gyro_deg_s[0], gyro_deg_s[1], gyro_deg_s[2], angular_acceleration[0], angular_acceleration[1], angular_acceleration[2]]
            
            # Insert data into the database, ID will auto-increment
            try:
                c.execute('INSERT INTO imu_data (timestamp, roll, pitch, yaw, quat_i, quat_j, quat_k, angular_velocity_x, angular_velocity_y, angular_velocity_z, angular_acceleration_x, angular_acceleration_y, angular_acceleration_z) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                          (current_time.isoformat(), *data))
                conn.commit()
            except Exception as e:
                print(f"Database insert error: {e}")

            # Print the Euler angles
            #if euler:
               # print(f"Euler angles: Roll={euler[0]}, Pitch={euler[1]}, Yaw={euler[2]}")


            last_time = current_time
            last_gyro = gyro_deg_s

        await asyncio.sleep(0.01)

    conn.close() #Close Connection to Database


async def main():
    data = []
    stop_event = asyncio.Event()
    imu_task = asyncio.create_task(read_imu_data(stop_event, data))

    #Open Connection to Database
    conn = sqlite3.connect(database)
    c = conn.cursor()


    end_time = datetime.now() + timedelta(seconds=195)
    while datetime.now() < end_time:
        if not data:
            await asyncio.sleep(0.05)
            continue


        # Assuming the Euler angle x is the first element in your data list
        y = data[2]

        vx = data[8] #Angular velocity

        # Assuming angular acceleration in x is part of the gyro data,
        # adjust the index based on your data structure
        ax = data[11]  # Adjust index as per your data array structure

        L = I * ax
        e =  y - target

        # Print the Euler angle x (as y) and error on the same line
        #print(f"\rEuler angle x (y): {y:.2f} degrees, Error (e): {e:.2f} degrees", end='', flush=True)

        # Print Euler angle x, angular velocity, angular acceleration, and error on the same line
        print(f"\rEuler angle x (y): {y:.2f} degrees, Angular velocity (vx): {vx:.5f}, "
              f"Angular acceleration (ax): {ax:.2f}, Error (e): {e:.2f}", end='', flush=False)


        s = kd * e + vx
        u = sign(s)

        
        # Insert control variables into the database
        c.execute('INSERT INTO control_log (timestamp, error, control_variable, control_action) VALUES (?, ?, ?, ?)',
                  (datetime.now().isoformat(), e, s, u))
        conn.commit()


        print()
       # print(u)

        if u == 1:
            await down_x(0.01)

        elif u == -1:
            await up_x(0.01)

        await asyncio.sleep(0.01)

    conn.close() #Close Connection to Database
    stop_event.set()
    await imu_task

asyncio.run(main())


