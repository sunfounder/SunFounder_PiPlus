#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global MIC
	'''
	initial the Sound Sensor module with SunFounder_PiPlus.Sound_Sensor()
	'''
	MIC = Sound_Sensor()

def main():
	while True:
		'''
		read()
		this function returns the value of microphone.
		value range from 0 to 255
		'''
		print MIC.read()

def destroy():
	MIC.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()
