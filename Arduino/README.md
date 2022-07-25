Steps for uploading and getting MPU data on Pi:
  1. Open Arduino IDE on your laptop/PC and Upload the IMUslave.ino code to the Arduino nano 
    a. If you do not know how to upload code, a tutorial is HERE> https://www.arduino.cc/en/Guide/ArduinoNano
  2. Once this is done, take your MPU 9250 and connect it to your nano (You will need to install the MPU9250 library in Arduino)
    a. Connections are > VCC->3V3 ; GND->GND ; SCL->A5 ; SDA->A4 (only 4 connections)
  3. After, plug the nano into the Pi via micro-USB (same one you powered the nano with)
  4. To check if the Pi reads the nano, open the terminal and type "/dev/tty*"...This searches for all devices and if the nano has a solid connections it will be shown      as ttyUSB0.
    a. If you do not have a connection, try replacing the cable or using a different nano.
  5. If you have a connection, make sure to install the libraries needed for the python code, if you do not already have them installed. Those include "sudo apt-get          install python3-pip" and "python3 -m pip install pyserial" into the Pi terminal
  6. After, save and run the IMUmaster.py code by typing "python3 IMUmaster.py" into the terminal.
    a. If you cannot save it, copy and paste the code by selecting the code and CTR+C to copy, then typing "nano IMUmaster.py" into the terminal and use CTR+SHIFT+V to          paste the code and save it. After, run the code by repeating the end of step 6.
  7. You should then recieve data from the MPU9250!! If not, repeat the steps and check your connections.
