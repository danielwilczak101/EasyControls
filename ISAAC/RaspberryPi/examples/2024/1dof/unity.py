import asyncio
import numpy as np
import sqlite3
import socket
from datetime import datetime, timedelta
from adafruit_bno055 import BNO055_I2C
from board import SCL, SDA
from busio import I2C
from enum import Enum
from contextlib import asynccontextmanager

# Database setup
database = 'imu_data.db'

def init_db():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS imu_data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp TEXT, roll REAL, pitch REAL, yaw REAL, 
                  quat_w REAL, quat_x REAL, quat_y REAL, quat_z REAL, 
                  angular_velocity_x REAL, angular_velocity_y REAL, angular_velocity_z REAL, 
                  angular_acceleration_x REAL, angular_acceleration_y REAL, angular_acceleration_z REAL)''')
    conn.commit()
    conn.close()

init_db()  # Initialize the database and table

# Constants and variables
m = 4
r = 0.2
kp = .7
ki = .5
kd = 1
target = 60
I = (m * r**2) / 4

# Enum for Solenoids
class Solinoid(Enum):
    TOP = 0
    BOTTOM = 1

# Enum for Thrusters
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

# TCP/IP Client Setup
def setup_tcp_client(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    return client

# Read IMU data and send it over TCP
async def read_imu_data(stop: asyncio.Event, tcp_client):
    # Setup for BNO055 sensor
    i2c = I2C(SCL, SDA)
    sensor = BNO055_I2C(i2c)

    while not stop.is_set():
        quat = sensor.quaternion  # Read quaternion from IMU
        if quat:
            data_str = f"{quat[0]},{quat[1]},{quat[2]},{quat[3]}"
            tcp_client.send(data_str.encode('utf-8'))
        await asyncio.sleep(0.1)  # Sleep to limit the rate of data sending

# Main asynchronous function to control the application
async def main():
    stop_event = asyncio.Event()
    tcp_client = setup_tcp_client('192.168.1.12', 25001)  # Set the IP and port
    try:
        imu_task = asyncio.create_task(read_imu_data(stop_event, tcp_client))
        await asyncio.sleep(30)  # Run for a limited time or integrate other stopping conditions
    finally:
        stop_event.set()
        await imu_task
        tcp_client.close()

asyncio.run(main())
