#include <Wire.h>
#include "MPU9250.h"

MPU9250 mpu;
int data = 0;
unsigned long previousMillis;

void setup() {
  
  Wire.begin(0x08);
  Serial.begin(9600);
 
  mpu.setup(0x68);
  
//  Serial.println("Calibrating Gyro");
//  mpu.calibrateAccelGyro();
//  Serial.println("Calibrating Mag");
//  mpu.calibrateMag();
//  Serial.println("Done Calibrating");
  Serial.println("Ready");
  Wire.onRequest(requestEvents);
}

void loop() {
  //if(checkTimePassed(100)){
     mpu.update();
     data = abs(mpu.getYaw());     
  //}
  
  delay(100);
}

void requestEvents(){
  Serial.println(data); 
  Wire.write(data);
}

boolean checkTimePassed(int inputInterval){  
  unsigned long currentMillis = millis();  
  if (currentMillis - previousMillis >= inputInterval) {
    previousMillis = currentMillis;
    return true;
  }
  return false; 
}
