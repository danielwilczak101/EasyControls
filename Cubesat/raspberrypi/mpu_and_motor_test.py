# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Display inclination data five times per second

# See this page to learn the math and physics principals behind this example:
# https://learn.adafruit.com/how-tall-is-it/gravity-and-acceleration

from this import d
import RPi.GPIO as GPIO
import time
from math import atan2, degrees
import board
import adafruit_mpu6050

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_mpu6050.MPU6050(i2c)

#Motor Setup
#Define pins
brakePin = 4
directionPin = 27
PWMPin = 13

#Pin Setup
#GPIO.setmode(GPIO.BOARD) #Use board numbering system (1-40)

GPIO.setup(brakePin, GPIO.OUT) #Defines this pin as output
GPIO.setup(directionPin, GPIO.OUT)
GPIO.setup(PWMPin, GPIO.OUT)

myPWM = GPIO.PWM(PWMPin,10000) #Sets PWM frequency to 20 kH

#Send high/low through pins
GPIO.output(brakePin, True) #True means high, False means low
GPIO.output(directionPin, False)

# Given a point (x, y) return the angle of that point relative to x axis.
# Returns: angle in degrees


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


# Given an accelerometer sensor object return the inclination angles of X/Z and Y/Z
# Returns: tuple containing the two angles in degrees


def get_inclination(_sensor):
    x, y, z = _sensor.acceleration
    return vector_2_degrees(x, z), vector_2_degrees(y, z)

#Stops motor in order to change direction

def brakeMotor():
    GPIO.output(brakePin, False)
    time.sleep(0.25)
    GPIO.output(brakePin, True)

#Start motor
myPWM.start(100) #0% duty cycle

#Calibrate angle "0"
angle_xz, angle_yz = get_inclination(sensor)
targetAngle = angle_yz
previousDirection = True
previousPWMDutyCycle = 100
print(targetAngle)

while True:
    angle_xz, angle_yz = get_inclination(sensor)
    print(angle_yz)
    if angle_yz < (targetAngle - 1): #angle_yz < targetAngle:
        currentDirection = True
        currentPWMDutyCycle = 99
    elif angle_yz > (targetAngle + 1):
        currentDirection = False
        currentPWMDutyCycle = 99
    else:
        currentDirection = True
        currentPWMDutyCycle = 100
    
    if currentDirection != previousDirection or currentPWMDutyCycle != previousPWMDutyCycle:
        brakeMotor()
        myPWM.ChangeDutyCycle(currentPWMDutyCycle)
        GPIO.output(directionPin, currentDirection)
        previousPWMDutyCycle = currentPWMDutyCycle
        previousDirection = currentDirection
    else:
        myPWM.ChangeDutyCycle(previousPWMDutyCycle)
        GPIO.output(directionPin, previousDirection)

    

