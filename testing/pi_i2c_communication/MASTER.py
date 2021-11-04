from smbus import SMBus

addr = 0x08 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

print ("For red, enter 1 for on or 0 for off")
print ("For green, enter 1 for on or 0 for off")
print ("Want to exit, enter Return")

while True:
	ledstate = input(">>  ") # entering the state of the LED [1, 2, or 0]
	if ledstate == "1":
		bus.write_byte_data(addr, 0x01, 1) # turning the red on
	elif ledstate == "0":
		bus.write_byte_data(addr, 0x01, 0) # turning the red off
	elif ledstate == "2":
		bus.write_byte_data(0x09, 0x10, 2) # turning the green on
	elif ledstate == "0":
		bus.write_byte_data(0x09, 0x10, 0) # turning the green off
	else:
		input("Press return to exit") # exiting the program, or stopping the while loop
		numb = 0




