auto analogPin = A1; // potentiometer wiper (middle terminal) connected to analog pin 1
                    // outside leads to ground and +5V
int input = 0;  // variable to store the value read
float scaled = 0;
void setup() {
  Serial.begin(9600);           //  setup serial
}

void loop() {
  input = analogRead(analogPin);  // read the input pin
  scaled = 0.36134 * input - 35.73916;
  Serial.println(scaled);          // debug value
  delay(1000);
}
