from this import d
import RPi.GPIO as GPIO
import time
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

myPWM = GPIO.PWM(PWMPin,10000) #Sets PWM frequency to 20 kH

#Send high/low through pins
GPIO.output(brakePin, True) #True means high, False means low
GPIO.output(directionPin, False)

#Start PWM
myPWM.start(50) #20% duty cycle

while 1:
    for i in range(20, 100):
        myPWM.ChangeDutyCycle(i)
        time.sleep(0.1)

    for i in range(100, 20):
        myPWM.ChangeDutyCycle(i)
        time.sleep(0.1)
        