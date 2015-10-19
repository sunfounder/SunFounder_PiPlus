#!/usr/bin/env python

'''
Module:
	It's a simple script for SunFounder PiPlus series.
	This script just simply converts the GPIOs from GPIO.BOARD to PIPLUS,
	so it depends on RPi.GPIO.
	Use this module like this:

		import RPi.GPIO as GPIO
		from SunFounder_PiPlus.PiPlus import *

		Buzzer = DB4

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(Buzzer, GPIO.OUT)
		
History:
	Version 1.0		Cavon Lee	 Oct.17 2015
'''

D0		=	7

DA1		=	11
DA2		=	12
DA3		=	13
DA4		=	15
DA5		=	16
DA6		=	18
DA7		=	22
DA8		=	29

DB1		=	31
DB2 	=	33
DB3 	=	35
DB4 	=	37
DB5 	=	32
DB6 	=	36
DB7 	=	38
DB8		=	40
	
CE0		=	24
CE1		=	26

SDA		=	3
SCL		=	5
TXD		=	8
RXD		=	10
MOSI	=	19
MISO	=	21
SCLK	=	23

AIN0	=	0
AIN1	=	1
AIN2	=	2
AIN3	=	3
