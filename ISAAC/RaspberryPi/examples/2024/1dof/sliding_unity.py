import asyncio
import numpy as np
import sqlite3
import socket
from datetime import datetime, timedelta
from enum import Enum
from adafruit_bno055 import BNO055_I2C
from board import SCL, SDA
from busio import I2C
from smbus2 import SMBus
from contextlib import asynccontextmanager

# Constants and global setup
database = 'imu_data.db'
i2c = I2C(SCL, SDA)
sensor = BNO055_I2C(i2c)
bus = SMBus(1)
kd = 1
target = 60
unity_ip = '192.168.1.12'  # Adjust to your Unity machine's IP
unity_port = 25001  # Adjust to the port you're listening on in Unity

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

    def __init__(self, address):
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
                bus.write_byte_data(thruster.address, solinoid.value, 0)
                thruster.is_open[solinoid.value] = False

def setup_tcp_client(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    return client

def init_db():
    with sqlite3.connect(database) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS imu_data
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      timestamp TEXT, roll REAL, pitch REAL, yaw REAL,
                      quat_w REAL, quat_i REAL, quat_j REAL, quat_k REAL,
                      angular_velocity_x REAL, angular_velocity_y REAL, angular_velocity_z REAL,
                      angular_acceleration_x REAL, angular_acceleration_y REAL, angular_acceleration_z REAL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS control_log
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      timestamp TEXT, kd REAL, target REAL, error REAL, control_variable REAL, control_action INTEGER)''')
        conn.commit()

async def read_imu_data(stop: asyncio.Event, shared_data: list, tcp_client):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    while not stop.is_set():
        quat = sensor.quaternion
        euler = sensor.euler
        gyro = np.array(sensor.gyro)
        if quat and euler and gyro is not None:
            current_time = datetime.now()
            data_str = f"{quat[0]},{quat[1]},{quat[2]},{quat[3]}\n"
            tcp_client.send(data_str.encode('utf-8'))
            c.execute('''INSERT INTO imu_data (timestamp, roll, pitch, yaw, quat_w, quat_i, quat_j, quat_k,
                        angular_velocity_x, angular_velocity_y, angular_velocity_z,
                        angular_acceleration_x, angular_acceleration_y, angular_acceleration_z)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                      (current_time.isoformat(), euler[0], euler[1], euler[2],
                       quat[0], quat[1], quat[2], quat[3], gyro[0], gyro[1], gyro[2], 0, 0, 0))
            conn.commit()
            shared_data[:] = [euler[0], euler[1], euler[2], quat[1], quat[2], quat[3], gyro[0], gyro[1], gyro[2], 0, 0, 0]
        await asyncio.sleep(0.1)
    conn.close() #Close Connection to Database

async def control_logic(stop_event, shared_data):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    while not stop_event.is_set():
        if shared_data:
            current_theta = shared_data[2]  # Assuming this is the yaw
            error = current_theta - target
            s = float(kd * error + shared_data[8])  # Using gyro's z component for angular velocity
            u = np.sign(s).astype(int)
            c.execute('''INSERT INTO control_log (timestamp, kd, target, error, control_variable, control_action)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (datetime.now().isoformat(), kd, target, error, s, u))
            conn.commit()
            if u == 1:
                await down_x(0.01)
            elif u == -1:
                await up_x(0.01)
        await asyncio.sleep(0.1)
    conn.close()

async def main():
    init_db()
    tcp_client = setup_tcp_client(unity_ip, unity_port)
    stop_event = asyncio.Event()
    shared_data = []
    imu_task = asyncio.create_task(read_imu_data(stop_event, shared_data, tcp_client))
    control_task = asyncio.create_task(control_logic(stop_event, shared_data))
    try:
        await asyncio.gather(imu_task, control_task)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        stop_event.set()
        tcp_client.close()
        await close_all()
        print("Cleaning up and closing solenoids...")

asyncio.run(main())
