#include <Wire.h>
#include <Adafruit_NeoPixel.h>
const int LEDPin = 25;
#define PIN 13 
#define NUMPIXELS 8
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int pixelSetA[4] = {0,1,2,3};
int pixelSetB[4] = {7,6,5,4};

int inputCount;
int states[2];
const int SOLS[2] = {9,12};
int SOLNum;

unsigned long previousMillis[2];

void setup() {
  Wire.begin(0x08);
  Serial.begin(9600);
  pinMode(SOLS[0], OUTPUT);
  pinMode(SOLS[1], OUTPUT);
  pinMode(LEDPin, OUTPUT);
  pixels.begin();
}

void loop() {
  Wire.onReceive(receiveData);
  fire();
  setPixels();
}

void receiveData(int howMany) {
  while (Wire.available()) {
    digitalWrite(LEDPin, HIGH);
    digitalWrite(LEDPin, LOW);
    
    //Reset inputCounter after reaching 2 inputs
//    if (inputCount == 2) {
//      inputCount = 0;
//    }

//From Pi (arduino_num, top/bottom on/off)
//First is sol to turn on
//Top = 0, Bottom = 1 AND Left = 0, Right = 1

    //Store the first input as the solenoid pin to turn on
    if(inputCount == 0){
      SOLNum = Wire.read();
      //Serial.println(SOLNum);
    }

    //Store the secound input as the duration in millis to keep the solenoid on
    if(inputCount == 1){
      states[SOLNum] = Wire.read();
      previousMillis[SOLNum] = millis();
      //Serial.println(states[SOLNum]);
      //Serial.println("");
    }

    inputCount += 1;
  }
  inputCount = 0;
}

void fire(){
  for(int i = 0; i < sizeof(SOLS)/2; i++){
    if(states[i] == 0){
      digitalWrite(SOLS[i], LOW);
    }
    if(states[i] == 1){
      digitalWrite(SOLS[i], HIGH);
    }

    //Open solenoid for 50 millis then close it
    if(states[i] == 2){
      if(checkTimePassed(i, 25)){
        digitalWrite(SOLS[i], LOW);
        states[i] = 0;
      }
      else{
        digitalWrite(SOLS[i], HIGH);
      }
    }
  }
}

void setPixels(){
  if(digitalRead(SOLS[0]) == 1){
    for(int i=0; i<4; i++) { // For each pixel... 
      pixels.setBrightness(10);    
      pixels.setPixelColor(pixelSetA[i], pixels.Color(0, 0, 255));
      pixels.show();   // Send the updated pixel colors to the hardware.
    }
  }

    if(digitalRead(SOLS[1]) == 1){
      for(int i=0; i<4; i++) { // For each pixel... 
        pixels.setBrightness(10);    
        pixels.setPixelColor(pixelSetB[i], pixels.Color(0, 0, 255));
        pixels.show();   // Send the updated pixel colors to the hardware.
      }
    }

   if(digitalRead(SOLS[0]) == 0){
      for(int i=0; i<4; i++) { // For each pixel... 
        pixels.setPixelColor(pixelSetA[i], pixels.Color(0, 0, 0));
        pixels.show();   // Send the updated pixel colors to the hardware.
      }
    }

  if(digitalRead(SOLS[1]) == 0){
    for(int i=0; i<4; i++) { // For each pixel...    
      pixels.setPixelColor(pixelSetB[i], pixels.Color(0, 0, 0));
      pixels.show();   // Send the updated pixel colors to the hardware.
    }
  }
}

boolean checkTimePassed(int i, int inputInterval){  
  unsigned long currentMillis = millis();  
  if (currentMillis - previousMillis[i] >= inputInterval) {
    // save the last time you blinked the LED
    previousMillis[i] = currentMillis;
    //Serial.print(inputInterval);
    //Serial.println(" PASSED");
    return true;
  }
  return false; 
}
