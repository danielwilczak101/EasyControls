## Test Requirements:
Wire up tank pressure reader. 
    - This can be done using an ardunio or raspberry pi.  
    
## Datasheet:
Model number = M3431-000006-300PG   
https://www.mouser.com/datasheet/2/418/8/ENG_DS_MSP340_B1-1130134.pdf

## Best fit function:
```
ŷ = 0.32007X - 23.6864
```

## Presure Test:
Data from pressue test(Pressue in psi = AnalogRead):  
```
0  = 102  
20 = 150
40 = 212
60 = 263
80 = 318
90 = 351
```

# Wiring
5v    - +  
Gnd   - Gnd  
White - Analog Pin  
