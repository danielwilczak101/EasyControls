# Make sure arduino is connected to Pi via USB

import serial

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
                x = data[1]
                y = data[0]
                z = data[2]

                print(f"x - {x: .0f},  y - {y: .0f}, z - {z: .0f}")
            except ValueError:
                print(line)
