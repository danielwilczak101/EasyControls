# AsteroidFreeFlier Overview:
Originally part of the NASA Asteroid flyer program has been repurposed by the EPPL to allow anyone interested in controls to go online and connect with a real working device and test their own control algorithms on a live device that is connected to the global internet. The spacecraft has been refitted with new and improved wiring, updated computers and a website that allows for members to connect and upload code to.

**Original purpose:**  
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



