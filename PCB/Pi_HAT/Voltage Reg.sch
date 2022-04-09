EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 2
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
L LM78M05CDTX_NOPB:LM78M05CDTX_NOPB VR1
U 1 1 6251FEBC
P 3780 3560
F 0 "VR1" H 3780 3927 50  0000 C CNN
F 1 "LM78M05CDTX_NOPB" H 3780 3836 50  0000 C CNN
F 2 ".pretty:TO228P991X255-3N" H 3780 3560 50  0001 L BNN
F 3 "" H 3780 3560 50  0001 L BNN
F 4 "102662" H 3780 3560 50  0001 L BNN "SNAPEDA_PACKAGE_ID"
F 5 "IPC-7351B" H 3780 3560 50  0001 L BNN "STANDARD"
F 6 "G" H 3780 3560 50  0001 L BNN "PARTREV"
F 7 "Texas Instruments" H 3780 3560 50  0001 L BNN "MANUFACTURER"
F 8 "2.55mm" H 3780 3560 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
	1    3780 3560
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Male J5
U 1 1 62520C86
P 5050 1600
F 0 "J5" V 4930 1500 50  0000 L CNN
F 1 "Power Supply" V 5000 1300 50  0000 L CNN
F 2 "TerminalBlock_RND:TerminalBlock_RND_205-00276_1x02_P5.00mm_Vertical" H 5050 1600 50  0001 C CNN
F 3 "~" H 5050 1600 50  0001 C CNN
	1    5050 1600
	0    1    1    0   
$EndComp
$Comp
L LM78M05CDTX_NOPB:LM78M05CDTX_NOPB VR2
U 1 1 62522320
P 5950 3530
F 0 "VR2" H 5950 3897 50  0000 C CNN
F 1 "LM78M05CDTX_NOPB" H 5950 3806 50  0000 C CNN
F 2 ".pretty:TO228P991X255-3N" H 5950 3530 50  0001 L BNN
F 3 "" H 5950 3530 50  0001 L BNN
F 4 "102662" H 5950 3530 50  0001 L BNN "SNAPEDA_PACKAGE_ID"
F 5 "IPC-7351B" H 5950 3530 50  0001 L BNN "STANDARD"
F 6 "G" H 5950 3530 50  0001 L BNN "PARTREV"
F 7 "Texas Instruments" H 5950 3530 50  0001 L BNN "MANUFACTURER"
F 8 "2.55mm" H 5950 3530 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
	1    5950 3530
	1    0    0    -1  
$EndComp
$Comp
L LM78M05CDTX_NOPB:LM78M05CDTX_NOPB VR3
U 1 1 62524929
P 8000 3530
F 0 "VR3" H 8000 3897 50  0000 C CNN
F 1 "LM78M05CDTX_NOPB" H 8000 3806 50  0000 C CNN
F 2 ".pretty:TO228P991X255-3N" H 8000 3530 50  0001 L BNN
F 3 "" H 8000 3530 50  0001 L BNN
F 4 "102662" H 8000 3530 50  0001 L BNN "SNAPEDA_PACKAGE_ID"
F 5 "IPC-7351B" H 8000 3530 50  0001 L BNN "STANDARD"
F 6 "G" H 8000 3530 50  0001 L BNN "PARTREV"
F 7 "Texas Instruments" H 8000 3530 50  0001 L BNN "MANUFACTURER"
F 8 "2.55mm" H 8000 3530 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
	1    8000 3530
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0101
U 1 1 62525296
P 4950 1880
F 0 "#PWR0101" H 4950 1730 50  0001 C CNN
F 1 "VCC" H 5060 1960 50  0000 C CNN
F 2 "" H 4950 1880 50  0001 C CNN
F 3 "" H 4950 1880 50  0001 C CNN
	1    4950 1880
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 625255A6
P 5050 1880
F 0 "#PWR0102" H 5050 1630 50  0001 C CNN
F 1 "GND" H 5180 1810 50  0000 C CNN
F 2 "" H 5050 1880 50  0001 C CNN
F 3 "" H 5050 1880 50  0001 C CNN
	1    5050 1880
	1    0    0    -1  
$EndComp
Wire Wire Line
	5050 1880 5050 1800
Wire Wire Line
	4950 1800 4950 1830
Wire Wire Line
	4950 1830 4910 1830
Connection ~ 4950 1830
Wire Wire Line
	4950 1830 4950 1880
Text GLabel 4880 1830 0    50   Input ~ 0
12V
Text GLabel 3040 3460 0    50   Input ~ 0
12V
$Comp
L power:GND #PWR0103
U 1 1 62527C50
P 4530 3660
F 0 "#PWR0103" H 4530 3410 50  0001 C CNN
F 1 "GND" V 4520 3480 50  0000 C CNN
F 2 "" H 4530 3660 50  0001 C CNN
F 3 "" H 4530 3660 50  0001 C CNN
	1    4530 3660
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3040 3460 3080 3460
Wire Wire Line
	3080 3460 3080 3130
Wire Wire Line
	3080 3130 5250 3130
Wire Wire Line
	5250 3130 5250 3430
Connection ~ 3080 3460
Wire Wire Line
	5250 3130 7300 3130
Wire Wire Line
	7300 3130 7300 3430
Connection ~ 5250 3130
Wire Wire Line
	4480 3460 5250 3460
Text HLabel 8700 3430 1    50   Input ~ 0
5V
$Comp
L power:GND #PWR0104
U 1 1 6252D5A1
P 6650 3630
F 0 "#PWR0104" H 6650 3380 50  0001 C CNN
F 1 "GND" V 6690 3480 50  0000 C CNN
F 2 "" H 6650 3630 50  0001 C CNN
F 3 "" H 6650 3630 50  0001 C CNN
	1    6650 3630
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 6252EF48
P 8840 3630
F 0 "#PWR0105" H 8840 3380 50  0001 C CNN
F 1 "GND" V 8910 3660 50  0000 C CNN
F 2 "" H 8840 3630 50  0001 C CNN
F 3 "" H 8840 3630 50  0001 C CNN
	1    8840 3630
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8700 3630 8780 3630
$Comp
L Connector:Conn_01x04_Male J4
U 1 1 62530307
P 3650 1780
F 0 "J4" H 3758 2061 50  0000 C CNN
F 1 "Solenoid I2C" H 3758 1970 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 3650 1780 50  0001 C CNN
F 3 "~" H 3650 1780 50  0001 C CNN
	1    3650 1780
	1    0    0    -1  
$EndComp
Wire Wire Line
	4910 1830 4910 1760
Wire Wire Line
	4910 1760 4650 1760
Wire Wire Line
	4650 1760 4650 1680
Wire Wire Line
	4650 1680 3850 1680
Connection ~ 4910 1830
Wire Wire Line
	4910 1830 4880 1830
$Comp
L power:GND #PWR0106
U 1 1 625334FB
P 3850 1780
F 0 "#PWR0106" H 3850 1530 50  0001 C CNN
F 1 "GND" V 3890 1690 50  0000 R CNN
F 2 "" H 3850 1780 50  0001 C CNN
F 3 "" H 3850 1780 50  0001 C CNN
	1    3850 1780
	0    -1   -1   0   
$EndComp
Text HLabel 3850 1880 2    50   Input ~ 0
SDA
Text HLabel 3850 1980 2    50   Input ~ 0
SCL
$Comp
L Device:C C1
U 1 1 6253424F
P 4310 2620
F 0 "C1" H 4425 2666 50  0000 L CNN
F 1 "C" H 4425 2575 50  0000 L CNN
F 2 "Capacitor_THT:C_Rect_L7.0mm_W2.5mm_P5.00mm" H 4348 2470 50  0001 C CNN
F 3 "~" H 4310 2620 50  0001 C CNN
	1    4310 2620
	1    0    0    -1  
$EndComp
$Comp
L Device:CP C2
U 1 1 62537D63
P 9190 3590
F 0 "C2" H 9308 3636 50  0000 L CNN
F 1 "CP" H 9308 3545 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D4.0mm_P1.50mm" H 9228 3440 50  0001 C CNN
F 3 "~" H 9190 3590 50  0001 C CNN
	1    9190 3590
	1    0    0    -1  
$EndComp
Wire Wire Line
	4310 2470 4310 1760
Wire Wire Line
	4310 1760 4650 1760
Connection ~ 4650 1760
Wire Wire Line
	9190 3740 8780 3740
Wire Wire Line
	8780 3740 8780 3630
Connection ~ 8780 3630
Wire Wire Line
	8780 3630 8840 3630
$Comp
L power:PWR_FLAG #FLG0101
U 1 1 62533E89
P 4950 1880
F 0 "#FLG0101" H 4950 1955 50  0001 C CNN
F 1 "PWR_FLAG" H 4950 2053 50  0000 C CNN
F 2 "" H 4950 1880 50  0001 C CNN
F 3 "~" H 4950 1880 50  0001 C CNN
	1    4950 1880
	-1   0    0    1   
$EndComp
Connection ~ 4950 1880
Wire Wire Line
	7260 3430 7260 3800
Wire Wire Line
	9190 3430 9190 3440
Wire Wire Line
	8700 3430 9190 3430
Wire Wire Line
	6650 3430 7260 3430
Wire Wire Line
	5250 3460 5250 3790
Wire Wire Line
	6650 3430 6650 3540
Wire Wire Line
	6650 3540 6920 3540
Wire Wire Line
	6920 3540 6920 3790
Wire Wire Line
	5250 3790 6920 3790
Connection ~ 6650 3430
Wire Wire Line
	4480 3660 4510 3660
Wire Wire Line
	4310 3720 4510 3720
Wire Wire Line
	4510 3720 4510 3660
Wire Wire Line
	4310 2770 4310 3720
Connection ~ 4510 3660
Wire Wire Line
	4510 3660 4530 3660
Wire Wire Line
	8700 3430 8700 3600
Wire Wire Line
	8700 3600 8680 3600
Wire Wire Line
	8680 3600 8680 3800
Connection ~ 8700 3430
Wire Wire Line
	8680 3800 7260 3800
$Comp
L power:PWR_FLAG #FLG0102
U 1 1 6253D63C
P 8840 3630
F 0 "#FLG0102" H 8840 3705 50  0001 C CNN
F 1 "PWR_FLAG" V 8840 3758 50  0000 L CNN
F 2 "" H 8840 3630 50  0001 C CNN
F 3 "~" H 8840 3630 50  0001 C CNN
	1    8840 3630
	0    1    1    0   
$EndComp
Connection ~ 8840 3630
$EndSCHEMATC
