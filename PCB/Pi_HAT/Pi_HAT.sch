EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 2
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
L ARDUINO_NANO:ARDUINO_NANO TB1
U 1 1 621FE12D
P 4660 3640
F 0 "TB1" H 4660 5207 50  0000 C CNN
F 1 "ARDUINO_NANO" H 4660 5116 50  0000 C CNN
F 2 ".pretty:SHIELD_ARDUINO_NANO" H 4660 3640 50  0001 L BNN
F 3 "" H 4660 3640 50  0001 L BNN
	1    4660 3640
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x10 J1
U 1 1 62208CE6
P 2610 3570
F 0 "J1" H 2528 2845 50  0000 C CNN
F 1 "MPU9250" H 2528 2936 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x10_P2.54mm_Vertical" H 2610 3570 50  0001 C CNN
F 3 "~" H 2610 3570 50  0001 C CNN
	1    2610 3570
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_02x03_Odd_Even J3
U 1 1 6220A503
P 7760 2870
F 0 "J3" H 7810 3187 50  0000 C CNN
F 1 "Display" H 7810 3096 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical" H 7760 2870 50  0001 C CNN
F 3 "~" H 7760 2870 50  0001 C CNN
	1    7760 2870
	1    0    0    -1  
$EndComp
NoConn ~ 2810 3470
NoConn ~ 2810 3370
NoConn ~ 2810 3270
NoConn ~ 2810 3170
NoConn ~ 2810 3070
Text GLabel 2810 3970 2    50   Input ~ 0
3.3VN
Text GLabel 2810 3770 2    50   Input ~ 0
SCLN
Text GLabel 2810 3670 2    50   Input ~ 0
SDAN
NoConn ~ 2810 3570
Text GLabel 3960 3440 0    50   Input ~ 0
SDAN
Text GLabel 3960 3540 0    50   Input ~ 0
SCLN
Text GLabel 7560 2730 0    50   Input ~ 0
3.3VP
Text GLabel 6490 2710 0    50   Input ~ 0
3.3VP
NoConn ~ 3960 2740
NoConn ~ 3960 3040
NoConn ~ 3960 3140
NoConn ~ 3960 3240
NoConn ~ 3960 3340
NoConn ~ 3960 3640
NoConn ~ 3960 3740
NoConn ~ 3960 3940
NoConn ~ 3960 4040
NoConn ~ 3960 4140
NoConn ~ 3960 4240
NoConn ~ 3960 4340
NoConn ~ 3960 4440
NoConn ~ 3960 4540
NoConn ~ 5360 4540
NoConn ~ 5360 4440
NoConn ~ 5360 4340
NoConn ~ 5360 4240
NoConn ~ 5360 4140
NoConn ~ 5360 3940
NoConn ~ 5360 4040
NoConn ~ 5360 2540
NoConn ~ 5360 2340
NoConn ~ 6490 3060
NoConn ~ 6490 3160
NoConn ~ 6490 3260
NoConn ~ 6490 3360
NoConn ~ 6490 3460
NoConn ~ 6490 3560
NoConn ~ 6490 3660
NoConn ~ 6490 3760
NoConn ~ 6490 3860
NoConn ~ 6490 3960
NoConn ~ 6490 4060
NoConn ~ 6490 4160
NoConn ~ 6490 4260
NoConn ~ 6490 4360
NoConn ~ 6490 4460
NoConn ~ 6490 4560
NoConn ~ 6490 4660
NoConn ~ 6990 4660
NoConn ~ 6990 4560
NoConn ~ 6990 4460
NoConn ~ 6990 4360
NoConn ~ 6990 4260
NoConn ~ 6990 4160
NoConn ~ 6990 4060
NoConn ~ 6990 3960
NoConn ~ 6990 3860
NoConn ~ 6990 3760
NoConn ~ 6990 3660
NoConn ~ 6990 3560
NoConn ~ 6990 3460
NoConn ~ 6990 3260
NoConn ~ 6990 3160
NoConn ~ 6990 3060
$Comp
L Mechanical:MountingHole H1
U 1 1 6221F507
P 5470 1240
F 0 "H1" H 5570 1286 50  0000 L CNN
F 1 "MountingHole" H 5570 1195 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 5470 1240 50  0001 C CNN
F 3 "~" H 5470 1240 50  0001 C CNN
	1    5470 1240
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 6221F7D0
P 5800 1240
F 0 "H2" H 5900 1286 50  0000 L CNN
F 1 "MountingHole" H 5900 1195 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 5800 1240 50  0001 C CNN
F 3 "~" H 5800 1240 50  0001 C CNN
	1    5800 1240
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 6222000C
P 6100 1240
F 0 "H3" H 6200 1286 50  0000 L CNN
F 1 "MountingHole" H 6200 1195 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 6100 1240 50  0001 C CNN
F 3 "~" H 6100 1240 50  0001 C CNN
	1    6100 1240
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 62220292
P 6400 1230
F 0 "H4" H 6500 1276 50  0000 L CNN
F 1 "MountingHole" H 6500 1185 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 6400 1230 50  0001 C CNN
F 3 "~" H 6400 1230 50  0001 C CNN
	1    6400 1230
	1    0    0    -1  
$EndComp
Text GLabel 5360 2440 2    50   Input ~ 0
3.3VN
$Sheet
S 8130 4100 2690 1570
U 6251FA46
F0 "Voltage Reg" 50
F1 "Voltage Reg.sch" 50
F2 "5V" I L 8130 4310 50 
F3 "SDA" I L 8130 4530 50 
F4 "SCL" I L 8130 4750 50 
$EndSheet
$Comp
L power:GND #PWR0107
U 1 1 62525DEF
P 6990 2960
F 0 "#PWR0107" H 6990 2710 50  0001 C CNN
F 1 "GND" V 6940 2890 50  0000 R CNN
F 2 "" H 6990 2960 50  0001 C CNN
F 3 "" H 6990 2960 50  0001 C CNN
	1    6990 2960
	0    -1   -1   0   
$EndComp
Text Label 8000 4310 0    50   ~ 0
5V
Wire Wire Line
	8130 4310 8000 4310
Wire Wire Line
	7120 2860 6990 2860
Wire Wire Line
	8130 4530 7980 4530
Text Label 7980 4530 0    50   ~ 0
SDA
Text Label 7980 4750 0    50   ~ 0
SCL
Wire Wire Line
	7980 4750 8130 4750
Text Label 7120 2860 2    50   ~ 0
5V
Text Label 7120 2760 2    50   ~ 0
5V
Wire Wire Line
	7120 2760 6990 2760
$Comp
L Connector_Generic:Conn_02x20_Odd_Even J2
U 1 1 622008CC
P 6690 3660
F 0 "J2" H 6740 4777 50  0000 C CNN
F 1 "Pi_GPIO" H 6740 4686 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical" H 6690 3660 50  0001 C CNN
F 3 "~" H 6690 3660 50  0001 C CNN
	1    6690 3660
	1    0    0    -1  
$EndComp
Wire Wire Line
	8190 2870 8060 2870
Text Label 8190 2870 2    50   ~ 0
5V
Text Label 8190 2770 2    50   ~ 0
5V
Wire Wire Line
	8190 2770 8060 2770
Wire Wire Line
	6490 2860 6300 2860
Text Label 6300 2860 0    50   ~ 0
SDA
Wire Wire Line
	6490 2710 6490 2760
Wire Wire Line
	6490 2960 6300 2960
Text Label 6300 2960 0    50   ~ 0
SCL
Wire Wire Line
	7560 2870 7370 2870
Text Label 7370 2870 0    50   ~ 0
SDA
Wire Wire Line
	7560 2970 7370 2970
Text Label 7370 2970 0    50   ~ 0
SCL
Wire Wire Line
	7560 2770 7560 2730
$Comp
L power:GND #PWR0108
U 1 1 6252CDEE
P 8060 2970
F 0 "#PWR0108" H 8060 2720 50  0001 C CNN
F 1 "GND" V 8010 2900 50  0000 R CNN
F 2 "" H 8060 2970 50  0001 C CNN
F 3 "" H 8060 2970 50  0001 C CNN
	1    8060 2970
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0109
U 1 1 6252D96E
P 5360 4940
F 0 "#PWR0109" H 5360 4690 50  0001 C CNN
F 1 "GND" V 5310 4870 50  0000 R CNN
F 2 "" H 5360 4940 50  0001 C CNN
F 3 "" H 5360 4940 50  0001 C CNN
	1    5360 4940
	0    -1   -1   0   
$EndComp
NoConn ~ 6990 3360
$Comp
L power:GND #PWR0110
U 1 1 6252EDEC
P 2810 3870
F 0 "#PWR0110" H 2810 3620 50  0001 C CNN
F 1 "GND" V 2810 3770 50  0000 R CNN
F 2 "" H 2810 3870 50  0001 C CNN
F 3 "" H 2810 3870 50  0001 C CNN
	1    2810 3870
	0    -1   -1   0   
$EndComp
NoConn ~ 3960 2840
$EndSCHEMATC
