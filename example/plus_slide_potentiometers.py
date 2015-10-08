#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global SP
	'''
	Initialize the Slide Potentiometers module with SunFounder_PiPlus.Slide_Potentiometers()
	'''
	SP = Slide_Potentiometers()

def main():
	while True:
		'''
		get_value(*sp)
		to get the specific potentiometer's value by argument *sp which ranges from 1 to 3.
		The argument should better be less than 3, but MUST comply with the potentiometers.
		For example:
		sp1 = SP.get_value(1)
		sp1, sp2 = SP.get_value(1, 2)
		sp3 = SP.get_value(3)
		sp1, sp3 = SP.get_value(1, 3)
		sp1, sp2, sp3 = SP.get_value(1, 2, 3)
		
		'''
		sp1, sp2 = SP.get_value(1, 2)
		print sp1, sp2
		time.sleep(0.2)

def destroy():
	SP.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()
