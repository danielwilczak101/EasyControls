import max31856
import RPi.GPIO as GPIO

csPin = 17
misoPin = 9
mosiPin = 10
clkPin = 11

max = max31856.max31856(csPin, misoPin, mosiPin, clkPin)
while True:
    thermoTempC = max.readThermocoupleTemp()
    thermoTempF = (thermoTempC * 9.0/5.0) + 32
    print("Thermocouple Temp: %f degF" % thermoTempF)

GPIO.cleanup()