import RPi.GPIO as GPIO
import time
# import time #time.sleep(1) would pause code for 1 second

# Define pins
brakePin = 7
directionPin = 13
PWMPin = 33

# Pin Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # Use board numbering system (1-40)

GPIO.setup(brakePin, GPIO.OUT)  # Defines this pin as output
GPIO.setup(directionPin, GPIO.OUT)
GPIO.setup(PWMPin, GPIO.OUT)


myPWM = GPIO.PWM(PWMPin, 10000)  # Sets PWM frequency to 20 kH

# Send high/low through pins
GPIO.output(brakePin, True)  # True means high, False means low
GPIO.output(directionPin, False)

# Start PWM
myPWM.start(0)  # 0% duty cycle


try:
    for _ in range(5):
        print(10)
        myPWM.ChangeDutyCycle(10)
        time.sleep(2)

        print(100)
        myPWM.ChangeDutyCycle(20)
        time.sleep(2)

        print(0)
        myPWM.ChangeDutyCycle(30)
        time.sleep(2)

except KeyboardInterrupt:
    print("Stop motor and exit.")
except:
    print("Some error happened")
finally:
    myPWM.ChangeDutyCycle(0)
