# AsteroidFreeFlier Overview:
Embry Riddle EPPL working to upgrade NASA's astroid free flier control platform.  
https://www.nasa.gov/feature/extreme-access-flyer-to-take-planetary-exploration-airborne

### Current state:
<p align="center">
  <img width="300px" height="400px" src="https://github.com/danielwilczak101/AsteroidFreeFlier/blob/media/images/craft1010.JPG">
</p>

# Test still in progress:

#### 1.atmega328PAU_bootloader_program
Waiting on the new board to come in so we can test adding a bootloader with the new chips. We also need to test adding programs to the chips.

#### 2. pi_i2c_solinoid_test  
Test worked with one solinoid firing. This is because the I2C code for both python and ardunio is sloppy and requires more testing. Also couldn't get the LED to turn on using I2C communication.

#### 3. pi_imu  
Currently the imu doesnt use gravity vector to correct for drift. We also still need to validate all the readings.  

#### 4. pi_website  
Testing has not started but still figuring out how the website is going to work with the code being uploaded.  



