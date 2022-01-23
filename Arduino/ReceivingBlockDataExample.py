from smbus import SMBus
import time

addr = 0x08
bus = SMBus(1)

while True:
    try:
        
        #Reads data from Arduino starting at offset 0, and expecting 3 bytes, stores bytes in array
        blockData = bus.read_i2c_block_data(addr, 0, 3)        
        print(f'Data 1: {blockData[0]}')
        print(f'Data 2: {blockData[1]}')
        print(f'Data 3: {blockData[2]}')       
    except:
        print("remote i/o error")