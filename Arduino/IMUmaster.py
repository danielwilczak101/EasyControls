# Make sure arduino is connected to Pi via USB

import serial # importing the Serial library, install by entering python3 -m pip install pyserial in Pi terminal

print("Waiting on Arduino......")

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1) # enter ls /dev/tty* into terminal to know what your Serial device name is, baud rate, timeout for read operations
    ser.reset_input_buffer() # This will flush any byte that could already be in the input buffer at that point

    while True: # infinite loop looking for bytes
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip() # receives and reads all bytes and strings
            print(line)
