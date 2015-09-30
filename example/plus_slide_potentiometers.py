#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global SP
	'''
	initial the Slide Potentiometers module with SunFounder_PiPlus.Slide_Potentiometers()
	'''
	SP = Slide_Potentiometers()

def main():
	while True:
		'''
		get_value(*sp)
		get specific potentiometers' value by argumen *sp, range from 1 to 3.
		mount of argument better be less than 3, but MUST be the same as ...(help me out here)
		for example:
		sp1 = SP.get_valur(1)
		sp1, sp2 = SP.get_valur(1, 2)
		sp3 = SP.get_valur(3)
		sp1, sp3 = SP.get_valur(1, 3)
		sp1, sp2, sp3 = SP.get_valur(1, 2, 3)
		
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
