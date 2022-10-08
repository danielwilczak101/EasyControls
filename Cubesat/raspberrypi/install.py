# Only run this if you have wiped the drive. It's so that the motor doesnt start up
# when you first power it.

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.cleanup()

gpio_number = 13
GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("GPIO no " + str(gpio_number) + ": " + str(GPIO.input(gpio_number)))
