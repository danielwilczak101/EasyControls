// Include the Servo library 
#include <Servo.h> 

int servoPin = 2; 

Servo Servo1; 

void setup() { 
   Servo1.attach(servoPin); 
}
void loop(){ 

   // Wiring {
      PWM - white
      Orange - 5v
      Blue - Gnd

   // Perpindicular to the pipe / 
   Servo1.write(45); 
   delay(2000); 
   
  // Parrellel to the pipe
   Servo1.write(140); 
   delay(2000); 

}
