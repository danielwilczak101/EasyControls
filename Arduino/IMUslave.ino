#include <MPU9250.h> // Make sure to install this library: CTRL+SHIFT+I then search MPU9250
#include <Wire.h>

MPU9250 mpu; // References the library as variable mpu

void setup() {
    Serial.begin(115200); // Baud rate set for Serial monitor, change to your liking
    Wire.begin(); // Opens the wires to communicate to MPU

    if (!mpu.setup(0x68)) {  // Change to your own address
        while (1) {
            Serial.println("MPU connection failed. Please check your connection with `connection_check` example."); // RX->TX & TX->RX
            delay(5000);
        }
    }
    // calibrate anytime you want to
    Serial.println("Calibrating Gyro....");
    mpu.calibrateAccelGyro(); // Library function to Calibrate the x,y, and z axis'
    Serial.println("READY!");
    delay(500); 
}

void loop() { // Prints the data from the MPU into the Serial monitor using MPU and Serial libraries
       if (mpu.update()) {
        Serial.print("[ ");
        Serial.print(mpu.getYaw()); Serial.print(", ");
        Serial.print(mpu.getPitch()); Serial.print(", ");
        Serial.print(mpu.getRoll()); Serial.println(" ]");
       }
}
