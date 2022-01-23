#include <Wire.h>

byte IMUData[3] = {66,97,5};

void setup() {
  Wire.begin(0x08);
  Wire.onRequest(requestEvents);
}

void loop() {
}

void requestEvents(){
  Wire.write(IMUData, 3);
}
