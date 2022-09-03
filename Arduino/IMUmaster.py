# Make sure arduino is connected to Pi via USB

from multiprocessing.sharedctypes import Value
from time import sleep
import serial  # importing the Serial library, install by entering python3 -m pip install pyserial in Pi terminal

print("Waiting on Arduino......")

if __name__ == '__main__':
    # enter ls /dev/tty* into terminal to know what your Serial device name is, baud rate, timeout for read operations
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    # This will flush any byte that could already be in the input buffer at that point
    ser.reset_input_buffer()

    while True:  # infinite loop looking for bytes
        if ser.in_waiting > 0:
            # receives and reads all bytes and strings
            line = ser.readline().decode('utf-8').rstrip()
            try:
                data = [float(x.strip()) for x in line.strip("[]").split(",")]
                x = data[0]
                y = data[1]
                z = data[2]

                print(f"x - {x},  y - {y}, z - {z}")
            except ValueError:
                print(line)

        sleep(1)
