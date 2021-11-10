## Test Requirements:
Wire tank servo and open and close tank valve.   
    - Tank pressue is optional but please detail in readme.  
    - Does not require I2C communication to the chip.  

## Big things to note
```C++
// Perpindicular to the pipe 
Servo1.write(45); 
delay(2000); 
   
// Parrellel to the pipe
Servo1.write(140); 
```

## Wiring
PWM - white
Orange - 5v
Blue - Gnd

## File Requirements:
1.Ardunio Code.  
2.Wiring Diagram(Hand written or drawen out).
