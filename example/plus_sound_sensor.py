#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global MIC
	'''
	Initialize the Sound Sensor module with SunFounder_PiPlus.Sound_Sensor()
	'''
	MIC = Sound_Sensor()

def main():
	threshold = 200
	while True:
		'''
		read()
		to return the value of microphone.
		The value ranges from 0 to 255.
		'''
		sound_value = 0
		sound_value = MIC.read()
		if sound_value > threshold:
			print 'Detect Sound! Sound value =', sound_value

def destroy():
	MIC.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()
