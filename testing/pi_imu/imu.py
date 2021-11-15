import time
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

mpu = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None, 
    bus=1,
    gfs=GFS_1000, 
    afs=AFS_8G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)

# Problem helper
# https://electronics.stackexchange.com/questions/205658/converting-raw-gyro-l3gd20h-values-into-angles

# Package information
# https://pypi.org/project/mpu9250-jmdev/#How-To-Use

mpu.calibrateMPU6500() # Calibrate sensors
mpu.configure() # The calibration function resets the sensors, so you need to reconfigure them

abias = mpu.abias # Get the master accelerometer biases
abias_slave = mpu.abias_slave # Get the slave accelerometer biases
gbias = mpu.gbias # Get the master gyroscope biases
gbias_slave = mpu.gbias_slave # Get the slave gyroscope biases

def remove_bias(dx_dt, bias):
    if abs(dx_dt) < bias:
        return 0
    elif dx_dt > 0:
        return dx_dt - abs(bias)
    else:
        return dx_dt + abs(bias)

angle = 0
dx_dt_0 = mpu.readGyroscopeMaster()[0]
t0 = time.time()

while True:
    
    dx_dt = remove_bias(mpu.readGyroscopeMaster()[0], gbias[0])
    t = time.time()
    # changes over time:
    dt = t - t0
    dx_dt_avg = (dx_dt + dx_dt_0) / 2
    # integral of dx_dt * dt = dx:
    angle += dx_dt_avg * dt*-++++
    t0 = t
    dx_dt_0 = dx_dt
    
    print(f"angle: {angle}")
    
    time.sleep(0.2)

