#include <Adafruit_NeoPixel.h>

// Which pin on the Arduino is connected to the NeoPixels?
#define LED_PIN    2

// How many NeoPixels are attached to the Arduino?
#define LED_COUNT 8

// Tutorial
// https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-use

// Declare our NeoPixel strip object:
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop(){

// Turns on one at a time to show a runway effect.
for (int i = 0; i <= 8; i++) {
    strip.setPixelColor(i,244, 3, 252);
    delay(200);
    strip.show();
  }
  
strip.clear();
}
