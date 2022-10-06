from this import d
import RPi.GPIO as GPIO
#import time #time.sleep(1) would pause code for 1 second

#Define pins
brakePin = 7
directionPin = 13
PWMPin = 33

#Pin Setup
GPIO.setmode(GPIO.BOARD) #Use board numbering system (1-40)

GPIO.setup(brakePin, GPIO.OUT) #Defines this pin as output
GPIO.setup(directionPin, GPIO.OUT)
GPIO.setup(PWMPin, GPIO.OUT)

myPWM = GPIO.PWM(PWMPin,20000) #Sets PWM frequency to 20 kH

#Send high/low through pins
GPIO.output(brakePin, True) #True means high, False means low
GPIO.output(directionPin, True)

#Start PWM
myPWM.start(20) #20% duty cycle
