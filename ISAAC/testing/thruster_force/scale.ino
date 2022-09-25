///
//    FILE: HX_plotter.ino
//  AUTHOR: Rob Tillaart
// VERSION: 0.1.0
// PURPOSE: HX711 demo
//     URL: https://github.com/RobTillaart/HX711
//
// HISTORY:
// 0.1.0    2020-06-15 initial version
//

#include "HX711.h"

HX711 scale;

uint8_t dataPin = 6;
uint8_t clockPin = 7;

uint32_t start, stop;
volatile float f;
//declare a variable called length from fulcrum (from test side to pivot point) keep it in METERS
float LFF; 
float LCi;
float LCf;
float SF;

void setup()
{
  Serial.begin(115200);
  //input the length in meters for LFF
  LFF = .365;
  LCi = ((6.37492364 * LFF) - 1) ;

  //have a case in the event that zero is entered for LFF
  if (LCi == -1 ){
    LCf = 0;
   }
  else {
  LCf = abs(LCi) * 1685;
  }
  SF = 1685+LCf;  

  
  // Serial.println(__FILE__);
  // Serial.print("LIBRARY VERSION: ");
  // Serial.println(HX711_LIB_VERSION);
  // Serial.println();

  scale.begin(dataPin, clockPin);

  // TODO find a nice solution for this calibration..
  // loadcell factor 20 KG
  // scale.set_scale(127.15);
  // loadcell factor 5 KG
  scale.set_scale(SF);
  // reset the scale to zero = 0
  scale.tare();
  Serial.print(SF);
  Serial.print(LCi);
  Serial.print(LCf);
  
}

void loop()
{
  
  f = scale.get_units(5);
  Serial.println(f);
  delay(100);
}

// -- END OF FILE --
