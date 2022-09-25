#include <Adafruit_NeoPixel.h>
#include <Wire.h> 
#define LED_PIN    2
#define LED_COUNT 8

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

const int TOP = 2; // Top solinoid
const int BOTTOM = 3; // bottom solinoid

static_assert(LOW == 0, "Expecting LOW to be 0");
int state = 0;

void setup() {
  // Connection
  Wire.begin(0x9);             // Joining I2C bus with ADR 0x08
  Wire.onReceive(receiveData); // Registering the data 
  // Solinoid
  pinMode(TOP, OUTPUT); // Solenoid 1
  pinMode(BOTTOM, OUTPUT); // Solenoid 2
  digitalWrite(TOP, LOW); 
  digitalWrite(BOTTOM, LOW);
  // LED
  strip.begin();
  strip.show(); // Initialize all pixels to 'off' 
}

void loop() { // A delay so the data does not come in so fast
  delay(100); 
}

void receiveData(int howMany) { // Function for receiving data 
  while (Wire.available()) {    // Looping through all but last
    int c = Wire.read();        // Receiving Byte as Character for Red and Green

    if(c == 1){
      // Fire top solinoid and turn on top two leds
      digitalWrite(TOP, HIGH); 
      strip.setPixelColor(8, 255, 0, 255);
      strip.setPixelColor(7, 255, 0, 255);
      strip.show();
    } 
    
    if(c == 0){
      // turn off and clear leds
      digitalWrite(TOP, LOW);   // Turn Green LED off
      digitalWrite(BOTTOM, LOW);   // Turn Red LED off
      strip.clear();
    }

    if(c == 2){
      // Fire  bottom solinoid and turn on bottom two leds
      digitalWrite(BOTTOM, HIGH);
      strip.setPixelColor(0, 255, 0, 255);
      strip.setPixelColor(1, 255, 0, 255);
      strip.show();
    }
  }
}
