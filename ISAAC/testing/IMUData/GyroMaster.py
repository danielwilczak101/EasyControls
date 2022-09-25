from smbus import SMBus

import time

addr = 0x08 
bus = SMBus(1)


while True:
    try:
        data = bus.read_byte_data(addr, 1)
        #data = bus.read_byte(addr)
        #if (data > 0):
        print(f'Request: {data}')
        time.sleep(1)
    except:
        print("remote i/o error")
