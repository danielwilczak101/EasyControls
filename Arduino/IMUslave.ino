#include <MPU9250.h>
#include <Wire.h>

MPU9250 mpu;

void setup() {
    Serial.begin(115200);
    Wire.begin();

    if (!mpu.setup(0x68)) {  // change to your own address
        while (1) {
            Serial.println("MPU connection failed. Please check your connection with `connection_check` example.");
            delay(5000);
        }
    }
    // calibrate anytime you want to
    Serial.println("Calibrating Gyro....");
    mpu.calibrateAccelGyro();
    Serial.println("READY!");
    delay(500); 
}

void loop() {
       if (mpu.update()) {
        Serial.print("[ ");
        Serial.print(mpu.getYaw()); Serial.print(", ");
        Serial.print(mpu.getPitch()); Serial.print(", ");
        Serial.print(mpu.getRoll()); Serial.println(" ]");
       }
}
