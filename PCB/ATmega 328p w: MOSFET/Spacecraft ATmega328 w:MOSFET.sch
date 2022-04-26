EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MCU_Microchip_ATmega:ATmega328P-AU U1
U 1 1 61E841E3
P 2400 4425
F 0 "U1" H 1925 5950 50  0000 C CNN
F 1 "ATmega328P-AU" H 1950 5875 50  0000 C CNN
F 2 "Package_QFP:TQFP-32_7x7mm_P0.8mm" H 2400 4425 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega328_P%20AVR%20MCU%20with%20picoPower%20Technology%20Data%20Sheet%2040001984A.pdf" H 2400 4425 50  0001 C CNN
	1    2400 4425
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW1
U 1 1 61E86BE3
P 4450 4725
F 0 "SW1" H 4450 5010 50  0000 C CNN
F 1 "SW_Push" H 4450 4919 50  0000 C CNN
F 2 "Dylans_Footprints:PTS636SK25SMTRLFS" H 4450 4925 50  0001 C CNN
F 3 "~" H 4450 4925 50  0001 C CNN
	1    4450 4725
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R5
U 1 1 61E88CC2
P 4000 4625
F 0 "R5" H 4068 4671 50  0000 L CNN
F 1 "10k" H 4068 4580 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4000 4625 50  0001 C CNN
F 3 "~" H 4000 4625 50  0001 C CNN
	1    4000 4625
	1    0    0    -1  
$EndComp
Wire Wire Line
	4250 4725 4000 4725
$Comp
L power:+5V #PWR0101
U 1 1 61E8C74C
P 4000 4525
F 0 "#PWR0101" H 4000 4375 50  0001 C CNN
F 1 "+5V" H 4015 4698 50  0000 C CNN
F 2 "" H 4000 4525 50  0001 C CNN
F 3 "" H 4000 4525 50  0001 C CNN
	1    4000 4525
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 61E8D9B3
P 5000 4725
F 0 "#PWR0102" H 5000 4475 50  0001 C CNN
F 1 "GND" V 5005 4597 50  0000 R CNN
F 2 "" H 5000 4725 50  0001 C CNN
F 3 "" H 5000 4725 50  0001 C CNN
	1    5000 4725
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4650 4725 5000 4725
$Comp
L power:GND #PWR0103
U 1 1 61E8F4A9
P 2400 6050
F 0 "#PWR0103" H 2400 5800 50  0001 C CNN
F 1 "GND" H 2405 5877 50  0000 C CNN
F 2 "" H 2400 6050 50  0001 C CNN
F 3 "" H 2400 6050 50  0001 C CNN
	1    2400 6050
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 6050 2400 5925
Wire Wire Line
	3000 3825 3375 3825
Wire Wire Line
	3375 3825 3375 3750
Wire Wire Line
	3000 3925 3375 3925
Wire Wire Line
	3375 3925 3375 4050
$Comp
L Device:C_Small C3
U 1 1 61E94D57
P 4425 3750
F 0 "C3" V 4200 3575 50  0000 C CNN
F 1 "22pf" V 4287 3750 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 4425 3750 50  0001 C CNN
F 3 "~" H 4425 3750 50  0001 C CNN
	1    4425 3750
	0    1    1    0   
$EndComp
$Comp
L Device:C_Small C4
U 1 1 61E95EF9
P 4425 4050
F 0 "C4" V 4200 3900 50  0000 C CNN
F 1 "22pf" V 4287 4050 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 4425 4050 50  0001 C CNN
F 3 "~" H 4425 4050 50  0001 C CNN
	1    4425 4050
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 61E9730B
P 4850 4050
F 0 "#PWR0104" H 4850 3800 50  0001 C CNN
F 1 "GND" V 4855 3922 50  0000 R CNN
F 2 "" H 4850 4050 50  0001 C CNN
F 3 "" H 4850 4050 50  0001 C CNN
	1    4850 4050
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 61E97FA0
P 4875 3750
F 0 "#PWR0105" H 4875 3500 50  0001 C CNN
F 1 "GND" V 4880 3622 50  0000 R CNN
F 2 "" H 4875 3750 50  0001 C CNN
F 3 "" H 4875 3750 50  0001 C CNN
	1    4875 3750
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4875 3750 4525 3750
Wire Wire Line
	4850 4050 4525 4050
$Comp
L power:+5V #PWR0106
U 1 1 61E99CBE
P 2125 2400
F 0 "#PWR0106" H 2125 2250 50  0001 C CNN
F 1 "+5V" H 2140 2573 50  0000 C CNN
F 2 "" H 2125 2400 50  0001 C CNN
F 3 "" H 2125 2400 50  0001 C CNN
	1    2125 2400
	1    0    0    -1  
$EndComp
Text Label 3125 5025 0    50   ~ 0
TXD
Text Label 3125 4925 0    50   ~ 0
RXD
Wire Wire Line
	3125 4925 3000 4925
Wire Wire Line
	3000 5025 3125 5025
Text Label 3125 4725 0    50   ~ 0
Reset
$Comp
L power:GND #PWR0113
U 1 1 61EDBF1F
P 8875 1600
F 0 "#PWR0113" H 8875 1350 50  0001 C CNN
F 1 "GND" V 8880 1472 50  0000 R CNN
F 2 "" H 8875 1600 50  0001 C CNN
F 3 "" H 8875 1600 50  0001 C CNN
	1    8875 1600
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR0114
U 1 1 61EDCFE6
P 8875 1700
F 0 "#PWR0114" H 8875 1550 50  0001 C CNN
F 1 "VCC" V 8890 1827 50  0000 L CNN
F 2 "" H 8875 1700 50  0001 C CNN
F 3 "" H 8875 1700 50  0001 C CNN
	1    8875 1700
	0    -1   -1   0   
$EndComp
Text Label 8700 2850 2    50   ~ 0
MISO
Text Label 9200 2950 0    50   ~ 0
MOSI
$Comp
L power:+5V #PWR0115
U 1 1 61EEBAA9
P 9200 2850
F 0 "#PWR0115" H 9200 2700 50  0001 C CNN
F 1 "+5V" V 9215 2978 50  0000 L CNN
F 2 "" H 9200 2850 50  0001 C CNN
F 3 "" H 9200 2850 50  0001 C CNN
	1    9200 2850
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0116
U 1 1 61EEBAAF
P 9200 3050
F 0 "#PWR0116" H 9200 2800 50  0001 C CNN
F 1 "GND" V 9205 2922 50  0000 R CNN
F 2 "" H 9200 3050 50  0001 C CNN
F 3 "" H 9200 3050 50  0001 C CNN
	1    9200 3050
	0    -1   -1   0   
$EndComp
$Comp
L LM78M05CDTX_NOPB:LM78M05CDTX_NOPB VR1
U 1 1 61EEE531
P 6575 1475
F 0 "VR1" H 6575 1842 50  0000 C CNN
F 1 "LM78M05CDTX_NOPB" H 6575 1751 50  0000 C CNN
F 2 "footprints:TO228P991X255-3N" H 6575 1475 50  0001 L BNN
F 3 "" H 6575 1475 50  0001 L BNN
F 4 "102662" H 6575 1475 50  0001 L BNN "SNAPEDA_PACKAGE_ID"
F 5 "IPC-7351B" H 6575 1475 50  0001 L BNN "STANDARD"
F 6 "G" H 6575 1475 50  0001 L BNN "PARTREV"
F 7 "Texas Instruments" H 6575 1475 50  0001 L BNN "MANUFACTURER"
F 8 "2.55mm" H 6575 1475 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
	1    6575 1475
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0117
U 1 1 61F188A2
P 5375 1375
F 0 "#PWR0117" H 5375 1225 50  0001 C CNN
F 1 "VCC" V 5390 1502 50  0000 L CNN
F 2 "" H 5375 1375 50  0001 C CNN
F 3 "" H 5375 1375 50  0001 C CNN
	1    5375 1375
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5375 1375 5700 1375
$Comp
L power:GND #PWR0118
U 1 1 61F1AACA
P 7275 1850
F 0 "#PWR0118" H 7275 1600 50  0001 C CNN
F 1 "GND" V 7280 1722 50  0000 R CNN
F 2 "" H 7275 1850 50  0001 C CNN
F 3 "" H 7275 1850 50  0001 C CNN
	1    7275 1850
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0119
U 1 1 61F1C264
P 7625 1375
F 0 "#PWR0119" H 7625 1225 50  0001 C CNN
F 1 "+5V" V 7640 1503 50  0000 L CNN
F 2 "" H 7625 1375 50  0001 C CNN
F 3 "" H 7625 1375 50  0001 C CNN
	1    7625 1375
	0    1    1    0   
$EndComp
Wire Wire Line
	7275 1375 7625 1375
$Comp
L Device:CP1_Small C7
U 1 1 61F1F34E
P 7275 1475
F 0 "C7" H 7366 1521 50  0000 L CNN
F 1 "0.1uF" H 7366 1430 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 7275 1475 50  0001 C CNN
F 3 "~" H 7275 1475 50  0001 C CNN
	1    7275 1475
	1    0    0    -1  
$EndComp
$Comp
L Device:C C5
U 1 1 61F21560
P 5700 1700
F 0 "C5" H 5815 1746 50  0000 L CNN
F 1 "0.33 uF" H 5815 1655 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 5738 1550 50  0001 C CNN
F 3 "~" H 5700 1700 50  0001 C CNN
	1    5700 1700
	1    0    0    -1  
$EndComp
Connection ~ 7275 1375
Wire Wire Line
	7275 1575 7275 1850
Connection ~ 7275 1575
Wire Wire Line
	5700 1850 7275 1850
Connection ~ 7275 1850
Wire Wire Line
	5700 1550 5700 1375
Connection ~ 5700 1375
Wire Wire Line
	5700 1375 5875 1375
Text Label 3300 3525 2    50   ~ 0
MOSI
Text Label 3300 3625 2    50   ~ 0
MISO
Wire Wire Line
	3300 3525 3000 3525
Wire Wire Line
	3000 3625 3300 3625
Text Label 3300 3725 2    50   ~ 0
SCK
Wire Wire Line
	3300 3725 3000 3725
Text Label 8700 2950 2    50   ~ 0
SCK
$Comp
L Connector:Conn_01x03_Female J4
U 1 1 61EB56C1
P 9050 3450
F 0 "J4" H 9078 3476 50  0000 L CNN
F 1 "LED" H 9078 3385 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 9050 3450 50  0001 C CNN
F 3 "~" H 9050 3450 50  0001 C CNN
	1    9050 3450
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0120
U 1 1 61EBA4A0
P 8850 3550
F 0 "#PWR0120" H 8850 3400 50  0001 C CNN
F 1 "+5V" V 8865 3678 50  0000 L CNN
F 2 "" H 8850 3550 50  0001 C CNN
F 3 "" H 8850 3550 50  0001 C CNN
	1    8850 3550
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0121
U 1 1 61EBA4A6
P 8850 3450
F 0 "#PWR0121" H 8850 3200 50  0001 C CNN
F 1 "GND" V 8855 3322 50  0000 R CNN
F 2 "" H 8850 3450 50  0001 C CNN
F 3 "" H 8850 3450 50  0001 C CNN
	1    8850 3450
	0    1    1    0   
$EndComp
Text Label 8850 3350 2    50   ~ 0
LED
Text Label 3175 5425 2    50   ~ 0
LED
Wire Wire Line
	3175 5425 3000 5425
Text Label 3275 5525 2    50   ~ 0
Gate1
Text Label 3275 5625 2    50   ~ 0
Gate2
Wire Wire Line
	9300 4025 9750 4025
$Comp
L power:GND #PWR0122
U 1 1 61EE6F1D
P 9750 4025
F 0 "#PWR0122" H 9750 3775 50  0001 C CNN
F 1 "GND" V 9755 3897 50  0000 R CNN
F 2 "" H 9750 4025 50  0001 C CNN
F 3 "" H 9750 4025 50  0001 C CNN
	1    9750 4025
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_Small_US R6
U 1 1 61EE6F23
P 9200 4025
F 0 "R6" V 8995 4025 50  0000 C CNN
F 1 "300" V 9086 4025 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 9200 4025 50  0001 C CNN
F 3 "~" H 9200 4025 50  0001 C CNN
	1    9200 4025
	0    1    1    0   
$EndComp
$Comp
L Device:LED D5
U 1 1 61EE6F2F
P 8875 4025
F 0 "D5" H 8750 3850 50  0000 C CNN
F 1 "LED" H 8875 3925 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric" H 8875 4025 50  0001 C CNN
F 3 "~" H 8875 4025 50  0001 C CNN
	1    8875 4025
	-1   0    0    1   
$EndComp
Wire Wire Line
	9100 4025 9025 4025
$Comp
L power:+5V #PWR0123
U 1 1 61EE8229
P 8450 4025
F 0 "#PWR0123" H 8450 3875 50  0001 C CNN
F 1 "+5V" V 8465 4153 50  0000 L CNN
F 2 "" H 8450 4025 50  0001 C CNN
F 3 "" H 8450 4025 50  0001 C CNN
	1    8450 4025
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8450 4025 8725 4025
Text Label 8325 4375 0    50   ~ 0
TXD
Text Label 8325 4750 0    50   ~ 0
RXD
Wire Wire Line
	9300 4375 9750 4375
$Comp
L power:GND #PWR0124
U 1 1 61EF9868
P 9750 4375
F 0 "#PWR0124" H 9750 4125 50  0001 C CNN
F 1 "GND" V 9755 4247 50  0000 R CNN
F 2 "" H 9750 4375 50  0001 C CNN
F 3 "" H 9750 4375 50  0001 C CNN
	1    9750 4375
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_Small_US R7
U 1 1 61EF986E
P 9200 4375
F 0 "R7" V 8995 4375 50  0000 C CNN
F 1 "300" V 9086 4375 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 9200 4375 50  0001 C CNN
F 3 "~" H 9200 4375 50  0001 C CNN
	1    9200 4375
	0    1    1    0   
$EndComp
$Comp
L Device:LED D6
U 1 1 61EF9874
P 8875 4375
F 0 "D6" H 8750 4200 50  0000 C CNN
F 1 "LED" H 8875 4275 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric" H 8875 4375 50  0001 C CNN
F 3 "~" H 8875 4375 50  0001 C CNN
	1    8875 4375
	-1   0    0    1   
$EndComp
Wire Wire Line
	9100 4375 9025 4375
Wire Wire Line
	8325 4375 8725 4375
Wire Wire Line
	9300 4750 9750 4750
$Comp
L power:GND #PWR0125
U 1 1 61EFE3EA
P 9750 4750
F 0 "#PWR0125" H 9750 4500 50  0001 C CNN
F 1 "GND" V 9755 4622 50  0000 R CNN
F 2 "" H 9750 4750 50  0001 C CNN
F 3 "" H 9750 4750 50  0001 C CNN
	1    9750 4750
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_Small_US R8
U 1 1 61EFE3F0
P 9200 4750
F 0 "R8" V 8995 4750 50  0000 C CNN
F 1 "300" V 9086 4750 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 9200 4750 50  0001 C CNN
F 3 "~" H 9200 4750 50  0001 C CNN
	1    9200 4750
	0    1    1    0   
$EndComp
$Comp
L Device:LED D7
U 1 1 61EFE3F6
P 8875 4750
F 0 "D7" H 8750 4575 50  0000 C CNN
F 1 "LED" H 8875 4650 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric" H 8875 4750 50  0001 C CNN
F 3 "~" H 8875 4750 50  0001 C CNN
	1    8875 4750
	-1   0    0    1   
$EndComp
Wire Wire Line
	9100 4750 9025 4750
Wire Wire Line
	8325 4750 8725 4750
Wire Wire Line
	2400 2800 2400 2925
$Comp
L power:+5V #PWR0126
U 1 1 61F363EE
P 2725 2400
F 0 "#PWR0126" H 2725 2250 50  0001 C CNN
F 1 "+5V" H 2740 2573 50  0000 C CNN
F 2 "" H 2725 2400 50  0001 C CNN
F 3 "" H 2725 2400 50  0001 C CNN
	1    2725 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 2925 2500 2800
$Comp
L Device:CP1_Small C1
U 1 1 61F4B2BD
P 2225 2500
F 0 "C1" V 2325 2450 50  0000 L CNN
F 1 "100nF" V 2125 2350 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 2225 2500 50  0001 C CNN
F 3 "~" H 2225 2500 50  0001 C CNN
	1    2225 2500
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small C6
U 1 1 61F45BC8
P 3675 4825
F 0 "C6" H 3800 4875 50  0000 C CNN
F 1 "100nF" H 3875 4800 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3675 4825 50  0001 C CNN
F 3 "~" H 3675 4825 50  0001 C CNN
	1    3675 4825
	-1   0    0    1   
$EndComp
Text Label 3275 4525 2    50   ~ 0
SDA
Text Label 3275 4625 2    50   ~ 0
SCL
Wire Wire Line
	3275 4625 3000 4625
Wire Wire Line
	3000 4525 3275 4525
Text Label 8875 1400 2    50   ~ 0
SDA
Text Label 8875 1500 2    50   ~ 0
SCL
$Comp
L Connector_Generic:Conn_02x03_Odd_Even J3
U 1 1 61F9A9EE
P 8900 2950
F 0 "J3" H 8950 3267 50  0000 C CNN
F 1 "Bootloader Pins" H 8950 3176 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical" H 8900 2950 50  0001 C CNN
F 3 "~" H 8900 2950 50  0001 C CNN
	1    8900 2950
	1    0    0    -1  
$EndComp
NoConn ~ 1800 3425
NoConn ~ 1800 3525
NoConn ~ 1800 3225
NoConn ~ 3000 3325
NoConn ~ 3000 3425
NoConn ~ 3000 4125
NoConn ~ 3000 4225
NoConn ~ 3000 4325
NoConn ~ 3000 4425
$Comp
L Mechanical:MountingHole H1
U 1 1 620169B7
P 8375 5700
F 0 "H1" H 8475 5746 50  0000 L CNN
F 1 "MountingHole" H 8475 5655 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.2mm_M2" H 8375 5700 50  0001 C CNN
F 3 "~" H 8375 5700 50  0001 C CNN
	1    8375 5700
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 6201708A
P 8375 5975
F 0 "H2" H 8475 6021 50  0000 L CNN
F 1 "MountingHole" H 8475 5930 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.2mm_M2" H 8375 5975 50  0001 C CNN
F 3 "~" H 8375 5975 50  0001 C CNN
	1    8375 5975
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 62017A5E
P 9250 5975
F 0 "H4" H 9350 6021 50  0000 L CNN
F 1 "MountingHole" H 9350 5930 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.2mm_M2" H 9250 5975 50  0001 C CNN
F 3 "~" H 9250 5975 50  0001 C CNN
	1    9250 5975
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 62018076
P 9250 5700
F 0 "H3" H 9350 5746 50  0000 L CNN
F 1 "MountingHole" H 9350 5655 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.2mm_M2" H 9250 5700 50  0001 C CNN
F 3 "~" H 9250 5700 50  0001 C CNN
	1    9250 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 5525 3275 5525
Wire Wire Line
	3275 5625 3000 5625
Wire Wire Line
	2125 2400 2125 2500
Wire Wire Line
	2125 2500 2125 2800
Wire Wire Line
	2125 2800 2400 2800
Connection ~ 2125 2500
Wire Wire Line
	2325 2500 2425 2500
$Comp
L power:GND #PWR01
U 1 1 62547CCF
P 2425 2375
F 0 "#PWR01" H 2425 2125 50  0001 C CNN
F 1 "GND" V 2430 2247 50  0000 R CNN
F 2 "" H 2425 2375 50  0001 C CNN
F 3 "" H 2425 2375 50  0001 C CNN
	1    2425 2375
	-1   0    0    1   
$EndComp
Wire Wire Line
	2425 2375 2425 2500
Connection ~ 2425 2500
Connection ~ 2725 2500
Wire Wire Line
	2725 2500 2725 2400
Wire Wire Line
	2725 2800 2725 2500
$Comp
L Device:CP1_Small C2
U 1 1 61F47625
P 2625 2500
F 0 "C2" V 2525 2450 50  0000 L CNN
F 1 "100nF" V 2725 2350 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 2625 2500 50  0001 C CNN
F 3 "~" H 2625 2500 50  0001 C CNN
	1    2625 2500
	0    1    1    0   
$EndComp
Wire Wire Line
	2425 2500 2525 2500
Wire Wire Line
	2500 2800 2725 2800
$Comp
L power:GND #PWR02
U 1 1 6256E077
P 3675 4925
F 0 "#PWR02" H 3675 4675 50  0001 C CNN
F 1 "GND" V 3680 4797 50  0000 R CNN
F 2 "" H 3675 4925 50  0001 C CNN
F 3 "" H 3675 4925 50  0001 C CNN
	1    3675 4925
	1    0    0    -1  
$EndComp
$Comp
L New_Library:DMN4026SSD U2
U 1 1 62644D45
P 2750 1525
F 0 "U2" H 2800 2190 50  0000 C CNN
F 1 "DMN4026SSD" H 2800 2099 50  0000 C CNN
F 2 "Dylans_Footprints:SOIC127P600X150-8N" H 2800 1575 50  0001 C CNN
F 3 "" H 2800 1575 50  0001 C CNN
	1    2750 1525
	1    0    0    -1  
$EndComp
$Comp
L Device:D D2
U 1 1 62646219
P 4100 1200
F 0 "D2" H 4100 1125 50  0000 C CNN
F 1 "D" H 4100 1300 50  0000 C CNN
F 2 "Diode_SMD:D_1812_4532Metric" H 4100 1200 50  0001 C CNN
F 3 "~" H 4100 1200 50  0001 C CNN
	1    4100 1200
	-1   0    0    1   
$EndComp
$Comp
L power:VCC #PWR04
U 1 1 62646CF8
P 4425 1350
F 0 "#PWR04" H 4425 1200 50  0001 C CNN
F 1 "VCC" V 4440 1477 50  0000 L CNN
F 2 "" H 4425 1350 50  0001 C CNN
F 3 "" H 4425 1350 50  0001 C CNN
	1    4425 1350
	0    1    1    0   
$EndComp
$Comp
L Device:D D3
U 1 1 62648037
P 4100 1500
F 0 "D3" H 4100 1425 50  0000 C CNN
F 1 "D" H 4100 1600 50  0000 C CNN
F 2 "Diode_SMD:D_1812_4532Metric" H 4100 1500 50  0001 C CNN
F 3 "~" H 4100 1500 50  0001 C CNN
	1    4100 1500
	-1   0    0    1   
$EndComp
Wire Wire Line
	3100 1425 3575 1425
Wire Wire Line
	3575 1575 3100 1575
Wire Wire Line
	3100 1275 3575 1275
Wire Wire Line
	3100 1125 3575 1125
Wire Wire Line
	4425 1350 4425 1200
Wire Wire Line
	4425 1200 4250 1200
Wire Wire Line
	4250 1500 4425 1500
Wire Wire Line
	4425 1500 4425 1350
Connection ~ 4425 1350
Wire Wire Line
	3575 1425 3575 1500
Wire Wire Line
	3575 1125 3575 1200
Wire Wire Line
	3575 1200 3950 1200
Connection ~ 3575 1200
Wire Wire Line
	3575 1200 3575 1275
Wire Wire Line
	3950 1500 3575 1500
Connection ~ 3575 1500
Wire Wire Line
	3575 1500 3575 1575
Text Label 3725 1200 0    50   ~ 0
SOL1
Text Label 3725 1500 0    50   ~ 0
SOL2
$Comp
L Device:R_Small_US R2
U 1 1 6265ED45
P 1525 1275
F 0 "R2" V 1475 1175 50  0000 C CNN
F 1 "10k" V 1600 1275 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 1525 1275 50  0001 C CNN
F 3 "~" H 1525 1275 50  0001 C CNN
	1    1525 1275
	0    1    1    0   
$EndComp
$Comp
L Device:R_Small_US R3
U 1 1 6265FF21
P 1525 1575
F 0 "R3" V 1475 1475 50  0000 C CNN
F 1 "10k" V 1600 1575 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 1525 1575 50  0001 C CNN
F 3 "~" H 1525 1575 50  0001 C CNN
	1    1525 1575
	0    1    1    0   
$EndComp
Wire Wire Line
	1625 1575 2500 1575
Wire Wire Line
	1625 1275 2500 1275
$Comp
L power:GND #PWR03
U 1 1 62665646
P 900 1350
F 0 "#PWR03" H 900 1100 50  0001 C CNN
F 1 "GND" V 905 1222 50  0000 R CNN
F 2 "" H 900 1350 50  0001 C CNN
F 3 "" H 900 1350 50  0001 C CNN
	1    900  1350
	0    1    1    0   
$EndComp
Wire Wire Line
	900  1350 900  1275
Wire Wire Line
	900  1125 2500 1125
Wire Wire Line
	2500 1425 900  1425
Wire Wire Line
	900  1425 900  1350
Connection ~ 900  1350
Wire Wire Line
	1425 1275 900  1275
Connection ~ 900  1275
Wire Wire Line
	900  1275 900  1125
Wire Wire Line
	900  1425 900  1575
Wire Wire Line
	900  1575 1425 1575
Connection ~ 900  1425
Text Label 1850 1275 0    50   ~ 0
Gate1
Text Label 1850 1575 0    50   ~ 0
Gate2
Connection ~ 3800 4050
Connection ~ 3800 3750
Wire Wire Line
	3800 4050 4325 4050
Wire Wire Line
	3375 4050 3800 4050
Wire Wire Line
	3800 3750 4325 3750
Wire Wire Line
	3375 3750 3800 3750
$Comp
L Device:Crystal Y1
U 1 1 61E91463
P 3800 3900
F 0 "Y1" V 3754 4031 50  0000 L CNN
F 1 "Crystal" V 3845 4031 50  0000 L CNN
F 2 "Dylans_Footprints:XTAL_ECS-160-20-5PXDN-TR" H 3800 3900 50  0001 C CNN
F 3 "~" H 3800 3900 50  0001 C CNN
	1    3800 3900
	0    1    1    0   
$EndComp
Connection ~ 4000 4725
Connection ~ 3675 4725
Wire Wire Line
	3675 4725 4000 4725
Wire Wire Line
	3000 4725 3675 4725
NoConn ~ 3000 5325
NoConn ~ 3000 5225
NoConn ~ 3000 5125
NoConn ~ 3000 3225
Text Label 8700 3050 2    50   ~ 0
Reset
$Comp
L Connector:Conn_01x04_Female J2
U 1 1 6266F275
P 9075 2025
F 0 "J2" H 9103 2001 50  0000 L CNN
F 1 "I2C/Power_IN" H 9103 1910 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 9075 2025 50  0001 C CNN
F 3 "~" H 9075 2025 50  0001 C CNN
	1    9075 2025
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR05
U 1 1 626722A0
P 8875 2125
F 0 "#PWR05" H 8875 1875 50  0001 C CNN
F 1 "GND" V 8880 1997 50  0000 R CNN
F 2 "" H 8875 2125 50  0001 C CNN
F 3 "" H 8875 2125 50  0001 C CNN
	1    8875 2125
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR06
U 1 1 626722A6
P 8875 2225
F 0 "#PWR06" H 8875 2075 50  0001 C CNN
F 1 "VCC" V 8890 2352 50  0000 L CNN
F 2 "" H 8875 2225 50  0001 C CNN
F 3 "" H 8875 2225 50  0001 C CNN
	1    8875 2225
	0    -1   -1   0   
$EndComp
Text Label 8875 1925 2    50   ~ 0
SDA
Text Label 8875 2025 2    50   ~ 0
SCL
$Comp
L Connector:Conn_01x04_Female J1
U 1 1 6264E8FA
P 9075 1500
F 0 "J1" H 9103 1476 50  0000 L CNN
F 1 "I2C/Power_IN" H 9103 1385 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 9075 1500 50  0001 C CNN
F 3 "~" H 9075 1500 50  0001 C CNN
	1    9075 1500
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Female J6
U 1 1 62683FCB
P 9075 1025
F 0 "J6" H 9103 1001 50  0000 L CNN
F 1 "SOL_2" H 9103 910 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 9075 1025 50  0001 C CNN
F 3 "~" H 9075 1025 50  0001 C CNN
	1    9075 1025
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Female J5
U 1 1 62685352
P 9075 725
F 0 "J5" H 9103 701 50  0000 L CNN
F 1 "SOL_1" H 9103 610 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 9075 725 50  0001 C CNN
F 3 "~" H 9075 725 50  0001 C CNN
	1    9075 725 
	1    0    0    -1  
$EndComp
Text Label 8875 1125 2    50   ~ 0
SOL2
Text Label 8875 825  2    50   ~ 0
SOL1
$Comp
L power:VCC #PWR08
U 1 1 62686B44
P 8875 1025
F 0 "#PWR08" H 8875 875 50  0001 C CNN
F 1 "VCC" V 8890 1152 50  0000 L CNN
F 2 "" H 8875 1025 50  0001 C CNN
F 3 "" H 8875 1025 50  0001 C CNN
	1    8875 1025
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR07
U 1 1 626887FB
P 8875 725
F 0 "#PWR07" H 8875 575 50  0001 C CNN
F 1 "VCC" V 8890 852 50  0000 L CNN
F 2 "" H 8875 725 50  0001 C CNN
F 3 "" H 8875 725 50  0001 C CNN
	1    8875 725 
	0    -1   -1   0   
$EndComp
$EndSCHEMATC
