#include <Wire.h> 
const int RED = 9; // Red LED pin
const int GRN = 8; // Green LED pin
static_assert(LOW == 0, "Expecting LOW to be 0");

void setup() {
  Wire.begin(0x8);             // Joining I2C bus with ADR 0x08
  Wire.onReceive(receiveData); // Registering the data 
  pinMode(RED, OUTPUT);
  digitalWrite(RED, LOW); 
  pinMode(GRN, OUTPUT);
  digitalWrite(GRN, LOW); 
}

void loop() {
  delay(100); 
}

void receiveData(int howMuch) {
  while (Wire.available()) {   // Looping through all but last
    char c = Wire.read();      // Receiving Byte as Character for Red
    char v = Wire.read();      // Receiving Byte as Character for Green
    digitalWrite(RED, c);
    digitalWrite(GRN, v);
  }
}
