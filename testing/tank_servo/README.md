## Test Requirements:
Wire tank servo and open and close tank valve.   
    - Tank pressue is optional but please detail in readme.  
    - Does not require I2C communication to the chip.  

## Big things to note
```C++
// Perpindicular to the pipe 
Servo1.write(45); 
   
// Parrellel to the pipe
Servo1.write(140); 
```

## Wiring
```
White  - PWM
Orange - 5v
Blue   - Gnd
```

## Image
![Wiring Breadboard](images/1.JPG)
