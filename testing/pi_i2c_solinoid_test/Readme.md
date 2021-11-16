## Test:
Test fire solinoid using i2c.

## Problem:
LED would not turn on and I2C code is poorly understood and written.

## Wiring:
Wiring was a combination of i2c wiring and solinoid firing.

## Code:

**File** i2c_solioid.ino is used for connection and firing on the ardunio. [Python code was the same from i2c testing](#).  

The code below was used to ensure solinoid fire properly.  
```C++
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(2, OUTPUT); // Solenoid 1
  pinMode(3, OUTPUT); // Solenoid 2
}

int sleep = 1000;

// the loop function runs over and over again forever
void loop() {
  digitalWrite(2, HIGH);   // Open Solenoid 1
  delay(sleep);                       // wait for a second
  digitalWrite(2, LOW);    // Open Close 1
  delay(sleep);                       // wait for a second
  digitalWrite(3, HIGH);   // Open Solenoid 2
  delay(sleep);                       // wait for a second
  digitalWrite(3, LOW);    // Open Close 2
  delay(sleep);                       // wait for a second
}
```




