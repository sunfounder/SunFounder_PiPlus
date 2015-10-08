#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global PR
	'''
	Initialize the Photoresistor module with SunFounder_PiPlus.Photoresistor()
	'''
	PR = Photoresistor()

def main():
	while True:
		'''
		brightness()
		to get the value of light intensity, which ranges from 0 to 255
		'''
		print PR.brightness()

def destroy():
	PR.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()
