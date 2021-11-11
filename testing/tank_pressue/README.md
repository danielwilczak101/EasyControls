## Test Requirements:
Wire up tank pressure reader. 
    - This can be done using an ardunio or raspberry pi.  
    
## Datasheet:

#### PS1,PS2
Model number = M3431-000006-300PG   
https://www.mouser.com/datasheet/2/418/8/ENG_DS_MSP340_B1-1130134.pdf

#### PS3
MLH03KPSB06A   
https://sensing.honeywell.com/index.php?&ci_id=31523&la_id=1 



## Fit functions:
```
// PS1 and PS2
ŷ = 0.32007X - 23.6864

// PS3
ŷ = 3.56029X - 357.29932;
```


## Presure Test PS1,PS2:
Data from pressue test(Pressue in psi = AnalogRead):  
```
// PS1 and PS2
0  = 102  
20 = 150
40 = 212
60 = 263
80 = 318
90 = 351

// PS3
0  = 101
20 = 105
40 = 112
60 = 117
80 = 123
95 = 127
```


# Wiring
5v    - +  
Gnd   - Gnd  
White - Analog Pin  
