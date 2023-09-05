#include <Wire.h> 
const int RED = 13; // Red LED pin
const int GRN = 5; // Green LED pin

static_assert(LOW == 0, "Expecting LOW to be 0");
int state = 0;

void setup() {
  Wire.begin(0x9);             // Joining I2C bus with ADR 0x08
  Wire.onReceive(receiveData); // Registering the data 
  pinMode(RED, OUTPUT);
  pinMode(GRN, OUTPUT);
  digitalWrite(RED, LOW); 
  digitalWrite(GRN, LOW); 
}

void loop() { // A delay so the data does not come in so fast
  delay(1000); 
}

void receiveData(int howMany) { // Function for receiving data 

  while (Wire.available()) {    // Looping through all but last
    int c = Wire.read();        // Receiving Byte as Character for Red and Green
    
    if(c == 1){
      digitalWrite(GRN, HIGH);  // Turn Green LED on 
    } 
    
    if(c == 0){
      digitalWrite(GRN, LOW);   // Turn Green LED off
      digitalWrite(RED, LOW);   // Turn Red LED off
    }

    if(c == 2){
      digitalWrite(RED, HIGH);  // Turn Red LED on
    }
  }
}
